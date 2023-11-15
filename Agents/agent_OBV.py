import gym
import numpy as np
import pandas as pd
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from finta import TA

# Custom Trading Environment based on OBV
class OBVTradingEnv(gym.Env):
    def __init__(self, df, window_size=12, initial_balance=1000):
        super(OBVTradingEnv, self).__init__()

        self.df = df
        self.window_size = window_size
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.current_step = 0

        # Action space (0: Hold, 1: Buy, 2: Sell)
        self.action_space = gym.spaces.Discrete(3)

        # Observation space (OBV values)
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(window_size, ), dtype=np.float64)

    def reset(self):
        self.balance = self.initial_balance
        self.current_step = 0
        return self._next_observation()

    def _next_observation(self):
        return self.df['OBV'][self.current_step:self.current_step+self.window_size].values

    def step(self, action):
        self.current_step += 1
        reward = 0
        done = self.current_step >= len(self.df) - self.window_size
        current_price = self.df['Close'].iloc[self.current_step]
        if action == 1:  # Buy
            self.balance -= current_price
            reward = 1  # Placeholder reward
        elif action == 2:  # Sell
            self.balance += current_price
            reward = 1  # Placeholder reward

        return self._next_observation(), reward, done, {}

    def render(self, mode='human'):
        print(f'Agent OBV Step: {self.current_step}, Balance: {self.balance}')

class OBVTradingAgent:
    def __init__(self, df):
        self.env = make_vec_env(lambda: OBVTradingEnv(df), n_envs=1)

        # Initialize the model
        self.model = A2C('MlpPolicy', self.env, verbose=1)

    def train_model(self, total_timesteps=10000):
        # Train the model
        self.model.learn(total_timesteps=total_timesteps)

    def predict(self, obs):
        # Use the model to predict the action based on the observation
        action, _states = self.model.predict(obs, deterministic=True)
        obs, rewards, dones, info = self.env.step(action)
        self.env.render()
        return action[0]