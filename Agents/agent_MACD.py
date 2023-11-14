import gym
import numpy as np
import pandas as pd
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from finta import TA

# Custom Trading Environment based on MACD
class MACDTradingAgent(gym.Env):
    def __init__(self, df, initial_balance=1000):
        super(MACDTradingAgent, self).__init__()

        self.df = df
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.current_step = 0

        # Action space (0: Hold, 1: Buy, 2: Sell)
        self.action_space = gym.spaces.Discrete(3)

        # Observation space (MACD, Signal, and Histogram values)
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(3, ), dtype=np.float64)

    def reset(self):
        self.balance = self.initial_balance
        self.current_step = 0
        return self._next_observation()

    def _next_observation(self):
        macd = self.df.iloc[self.current_step]['MACD']
        signal = self.df.iloc[self.current_step]['MACD_SIGNAL']
        histogram = self.df.iloc[self.current_step]['MACD_HIST']
        return np.array([macd, signal, histogram])

    def step(self, action):
        self.current_step += 1

        current_price = self.df['Close'][self.current_step]
        reward = 0
        done = self.current_step >= len(self.df) - 1

        if action == 1:  # Buy
            self.balance -= current_price
            reward = 1  # Placeholder reward
        elif action == 2:  # Sell
            self.balance += current_price
            reward = 1  # Placeholder reward

        return self._next_observation(), reward, done, {}

    def render(self, mode='human'):
        print(f'Step: {self.current_step}, Balance: {self.balance}')

# Load and preprocess data
df = pd.read_csv('data.csv')
macd = TA.MACD(df)
df['MACD'] = macd['MACD']
df['MACD_SIGNAL'] = macd['SIGNAL']
df['MACD_HIST'] = df['MACD'] - df['MACD_SIGNAL']
df.dropna(inplace=True)

# Create and check the environment
env = MACDTradingAgent(df)
env = make_vec_env(lambda: MACDTradingAgent(df), n_envs=1)

# Train the MACD model
model = A2C('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)

# Test the trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render()
