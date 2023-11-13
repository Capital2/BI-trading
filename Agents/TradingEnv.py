import gym
import numpy as np

class TradingEnvironment(gym.Env):
    def __init__(self, df, initial_balance=1000):
        super(TradingEnvironment, self).__init__()

        # DataFrame containing stock market data
        self.df = df
        self.current_step = 0
        self.balance = initial_balance
        self.shares_held = 0
        self.total_shares_sold = 0
        self.total_sales_value = 0

        # Define action and observation space
        self.action_space = gym.spaces.Discrete(3)  # 0: Hold, 1: Buy, 2: Sell
        self.observation_space = gym.spaces.Box(low=0, high=np.inf, shape=(len(df.columns),))

    def reset(self):
        self.balance = 1000  # Reset balance
        self.shares_held = 0
        self.total_shares_sold = 0
        self.total_sales_value = 0
        self.current_step = 0
        return self._next_observation()

    def _next_observation(self):
        return self.df.iloc[self.current_step].values

    def step(self, action):
        self.current_step += 1
        done = self.current_step >= len(self.df) - 1

        current_price = self.df.loc[self.current_step, 'Close']
        reward = 0

        if action == 1:  # Buy
            self.balance -= current_price  # Subtract cost from balance
            self.shares_held += 1

        elif action == 2 and self.shares_held > 0:  # Sell
            self.balance += current_price
            self.shares_held -= 1
            self.total_shares_sold += 1
            self.total_sales_value += current_price

        reward = self.balance - 1000  # Reward is the profit (or loss)

        return self._next_observation(), reward, done, {}

    def render(self, mode='human', close=False):
        profit = self.balance - 1000
        print(f'Step: {self.current_step}, Balance: {self.balance}, Shares held: {self.shares_held}, Total sold: {self.total_shares_sold}, Total sales value: {self.total_sales_value}, Profit: {profit}')
