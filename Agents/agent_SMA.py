import gym
import numpy as np
import pandas as pd
from stable_baselines3 import A2C
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_vec_env
from finta import TA

class SimpleMovingAverageAgent(gym.Env):
    def __init__(self, df, window_size=12, initial_balance=1000):
        super(SimpleMovingAverageAgent, self).__init__()

        self.df = df
        self.window_size = window_size
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.current_step = 0

        # Define action and observation space
        # Actions: 0 - Hold, 1 - Buy, 2 - Sell
        self.action_space = gym.spaces.Discrete(3)

        # Observation space: SMA values
        self.observation_space = gym.spaces.Box(low=0, high=np.inf, shape=(window_size, ), dtype=np.float64)

    def reset(self):
        self.balance = self.initial_balance
        self.current_step = 0
        return self._next_observation()

    def _next_observation(self):
        return self.df['SMA'][self.current_step:self.current_step+self.window_size].values

    def step(self, action):
        self.current_step += 1
        current_price = self.df['Close'][self.current_step]
        reward = 0
        done = self.current_step >= len(self.df) - self.window_size

        # Implement trading logic
        if action == 1:  # Buy
            # Example: Buy one unit and subtract from balance
            self.balance -= current_price
            reward = 1  # Placeholder reward
        elif action == 2:  # Sell
            # Example: Sell one unit and add to balance
            self.balance += current_price
            reward = 1  # Placeholder reward

        return self._next_observation(), reward, done, {}

    def render(self, mode='human'):
        print(f'Step: {self.current_step}, Balance: {self.balance}')

# Load and preprocess data
df = pd.read_csv('data.csv')
df['SMA'] = TA.SMA(df, 1)
df.dropna(inplace=True)

# Create and check the custom environment
env = SimpleMovingAverageAgent(df)
check_env(env)

# Vectorized environment for stable baselines
env = make_vec_env(lambda: SimpleMovingAverageAgent(df), n_envs=1)

# Train the model
model = A2C('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)

# Test the trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render()
