from agent_SMA import SimpleMovingAverageAgent
from agent_RSI import RSITradingAgent
from agent_MACD import MACDTradingAgent
from agent_OBV import OBVTradingAgent
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
df['MACD'] = TA.MACD(df)['MACD']
df['MACD_SIGNAL'] = TA.MACD(df)['SIGNAL']
df.fillna(0, inplace=True)

sma_agent = SimpleMovingAverageAgent(df)
obv_agent = OBVTradingAgent(df)
rsi_agent = RSITradingAgent(df)
macd_agent = MACDTradingAgent(df)
# Initialize master agent with the specialized agents

master_agent = MasterTradingAgent(sma_agent, rsi_agent, obv_agent, macd_agent)
master_agent.train_models()

action = master_agent.make_decision()
print(f"Action: {action}")
