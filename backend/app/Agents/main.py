from agent_SMA import SimpleMovingAverageAgent
from agent_RSI import RSITradingAgent
from agent_MACD import MACDTradingAgent
from agent_OBV import OBVTradingAgent
from agent_Master import MasterTradingAgent
import pandas as pd
from finta import TA

print("Here******")
# Load market data for the environment
df = pd.read_csv('data_btc.csv')
df['Date'] = pd.to_datetime(df['Timestamp']) 
df.set_index('Date', inplace=True)
df.sort_index(ascending=True, inplace=True)

df['Volume'] = df['Volume_(BTC)']
df['SMA'] = TA.SMA(df, 12) # 12 period simple moving average
df['RSI'] = TA.RSI(df)
df['OBV'] = TA.OBV(df)
df['MACD'] = TA.MACD(df)['MACD']
df['MACD_SIGNAL'] = TA.MACD(df)['SIGNAL']
df.fillna(0, inplace=True)
df.dropna(inplace=True)

# export dataframe to csv
df.to_csv('data_btc.csv')
print(df.info())

sma_agent = SimpleMovingAverageAgent(df)
obv_agent = OBVTradingAgent(df)
rsi_agent = RSITradingAgent(df)
macd_agent = MACDTradingAgent(df)
# Initialize master agent with the specialized agents

master_agent = MasterTradingAgent(sma_agent, rsi_agent, obv_agent, macd_agent)
master_agent.train_models()

master_agent.step(1000, 10)
# action = master_agent.make_decision()
# print(f"Action: {action}")
