from agent_SMA import SimpleMovingAverageAgent
# from agent_RSI import RSITradingAgent
# from agent_OBV import OBVTradingAgent
# from agent_MACD import MACDTradingAgent
from agent_Master import MasterTradingAgent
from TradingEnv import TradingEnvironment
import pandas as pd
from gym_anytrading.envs import StocksEnv 
from stable_baselines3.common.vec_env import DummyVecEnv
from finta import TA

print("Here******")
# Load market data for the environment
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date']) 
df.set_index('Date', inplace=True)
df.sort_index(ascending=True, inplace=True)
df['Volume'] = df['Volume'].apply(lambda x: float(x.replace(",", "")))
df['SMA'] = TA.SMA(df, 12) # 12 period simple moving average
df['RSI'] = TA.RSI(df)
df['OBV'] = TA.OBV(df)
df.fillna(0, inplace=True)
print(df)
# print(df)

# Initialize the trading environment
def my_process_data(env):
    start = env.frame_bound[0] - env.window_size # The first time step that we are going to use to train our model (the first value that we found in the frame_bound tuple)
    end = env.frame_bound[1] # The last time step that we are going to use to train our model (the second value that we found in the frame_bound tuple)
    prices = env.df.loc[:, 'Low'].to_numpy()[start:end] # Getting all the rows of the Low column, converting it to a numpy array and then slicing it from start to end
    signal_features = env.df.loc[:, ['Low', 'Volume','SMA', 'RSI', 'OBV']].to_numpy()[start:end] # We can choose what to bring in as features
    return prices, signal_features

class MyStocksEnv(StocksEnv):
    _process_data = my_process_data # Helps to access the features from outide the trading environment
    
env = MyStocksEnv(df=df, window_size=12, frame_bound=(80, 120))
print("Here2******")

# Initialize specialized agents
sma_agent = SimpleMovingAverageAgent(df)
print("Here3******")
# rsi_agent = RSITradingAgent(df)
# obv_agent = OBVTradingAgent(df)
# macd_agent = MACDTradingAgent(df)
# Initialize master agent with the specialized agents
master_agent = MasterTradingAgent(sma_agent, None, None, None)

print("Here3******")
# Run the trading simulation
state, info = env.reset()
# done = False
# while not done:
master_agent.train_models()
action = master_agent.make_decision(state)
print(f"Action: {action}")
state, reward, done, info = env.step(action)
env.render()
