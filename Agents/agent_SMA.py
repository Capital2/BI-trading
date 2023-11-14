import gym
import numpy as np
import pandas as pd
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env

class SimpleMovingAverageAgent(gym.Env):
    def __init__(self, df, window_size=5, initial_balance=1000):
        super(SimpleMovingAverageAgent, self).__init__()

        self.df = df
        self.window_size = window_size
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.current_step = 0

        # Action and observation space
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(low=0, high=np.inf, shape=(window_size,), dtype=np.float64)

        # Initialize the model to None, it will be set after training
        self.model = None

    def reset(self):
        self.balance = self.initial_balance
        self.current_step = 0
        return self._next_observation()

    def step(self, action):
        self.current_step += 1

        if self.current_step >= len(self.df):
            done = True
            reward = self.balance - self.initial_balance  # Final reward is the profit/loss
            return self._next_observation(), reward, done, {}

        current_price = self.df['Close'][self.current_step]
        reward = 0
        done = False

        if action == 1:  # Buy
            self.balance -= current_price
            reward = 1
        elif action == 2:  # Sell
            self.balance += current_price
            reward = 1

        return self._next_observation(), reward, done, {}

    def render(self, mode='human'):
        print(f'Step: {self.current_step}, Balance: {self.balance}')

    def train_model(self):
        # delete date column
        env = make_vec_env(lambda: self, n_envs=1)
        self.model = A2C('MlpPolicy', env, verbose=1)
        self.model.learn(total_timesteps=1000)

    def _next_observation(self):
        window_end = min(self.current_step + self.window_size, len(self.df))
        window_data = self.df['SMA'][self.current_step:window_end]
        
        # Ensure window_data is in a numeric format
        window_data = window_data.astype(np.float64)

        # Padding if the window is not filled yet
        padding = np.zeros(self.window_size - len(window_data))
        return np.concatenate((padding, window_data), axis=0)

    def predict(self, obs):
        obs = obs[np.newaxis, ...]
        if self.model is None:
            raise Exception("Model not loaded. Please load the model before prediction.")

        # if obs.shape[0] != self.window_size:
        #     raise ValueError(f"Expected observation shape {(self.window_size,)}, but got {obs.shape}")

        action, _states = self.model.predict(obs, deterministic=True)
        return action
