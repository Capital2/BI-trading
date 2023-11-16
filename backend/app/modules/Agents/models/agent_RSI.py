import gym
import numpy as np
import pandas as pd
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from finta import TA
from pathlib import Path
from pandas import DataFrame

# Custom Trading Environment based on RSI
class RSITradingEnv(gym.Env):
    def __init__(self, df, window_size=14, initial_balance=1000):
        super(RSITradingEnv, self).__init__()

        self.df = df
        self.window_size = window_size
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.current_step = 0

        # Action space (0: Hold, 1: Buy, 2: Sell)
        self.action_space = gym.spaces.Discrete(3)

        # Observation space (RSI values)
        self.observation_space = gym.spaces.Box(
            low=0, high=100, shape=(window_size,), dtype=np.float64
        )

    def reset(self):
        self.balance = self.initial_balance
        self.current_step = 0
        return self._next_observation()

    def _next_observation(self):
        return self.df["RSI"][
            self.current_step : self.current_step + self.window_size
        ].values

    def step(self, action):
        self.current_step += 1

        current_price = self.df["Close"][self.current_step]
        reward = 0
        done = self.current_step >= len(self.df) - self.window_size

        if action == 1:  # Buy
            self.balance -= current_price
            reward = 1  # Placeholder reward
        elif action == 2:  # Sell
            self.balance += current_price
            reward = 1  # Placeholder reward

        return self._next_observation(), reward, done, {}

    def render(self, mode="human"):
        print(f"Agent RSI Step: {self.current_step}, Balance: {self.balance}")


class RSITradingAgent:
    def __init__(self, df: DataFrame, share: str):
        self.env = make_vec_env(lambda: RSITradingEnv(df), n_envs=1)
        self.model = A2C("MlpPolicy", self.env, verbose=1)
        self.share = share

    def train_model(self, total_timesteps=10000):
        self.model.learn(total_timesteps=total_timesteps)
        self.model.save(
            Path.joinpath(
                Path.cwd(), "modules", "Agents", "artifacts", f"RSI_{self.share}.h5"
            )
        )

    def predict(self, obs):
        action, _states = self.model.predict(obs, deterministic=True)
        obs, rewards, dones, info = self.env.step(action)
        # self.env.render()
        return action[0]

    def evaluate(self, historical_signals):
        predicted_signals = [self.predict(obs) for obs in self.env.reset()]
        accuracy = sum(
            1
            for predicted, actual in zip(predicted_signals, historical_signals)
            if predicted == actual
        ) / len(historical_signals)
        return accuracy
