from agent_SMA import SimpleMovingAverageAgent
# from agent_RSI import RSITradingAgent
# from agent_OBV import OBVTradingAgent
# from agent_MACD import MACDTradingAgent
from agent_Master import MasterTradingAgent
from TradingEnv import TradingEnvironment
import pandas as pd

print("Here******")
# Load market data for the environment
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date']) 
df.set_index('Date', inplace=True)
df.sort_index(ascending=True, inplace=True)

print(df)
# print(df)

# Initialize the trading environment
env = TradingEnvironment(df)
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
state = env.reset()
# done = False
# while not done:
master_agent.train_models()
action = master_agent.make_decision(state)
print(f"Action: {action}")
state, reward, done, info = env.step(action)
env.render()
