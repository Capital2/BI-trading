from agent_SMA import SimpleMovingAverageAgent
from agent_RSI import RSITradingAgent
from agent_OBV import OBVTradingAgent
from agent_F7ima import MACDTradingAgent
from agent_bedis import MasterTradingAgent
from TradingEnv import TradingEnvironment
import pandas as pd

# Load market data for the environment
df = pd.read_csv('data.csv')
print(df)

# Initialize the trading environment
env = TradingEnvironment(df)

# Initialize specialized agents
sma_agent = SimpleMovingAverageAgent(df)
rsi_agent = RSITradingAgent(df)
obv_agent = OBVTradingAgent(df)
macd_agent = MACDTradingAgent(df)

# Initialize master agent with the specialized agents
master_agent = MasterTradingAgent(sma_agent, rsi_agent, obv_agent, macd_agent)

# Run the trading simulation
state = env.reset()
done = False
while not done:
    action = master_agent.make_decision(state)
    state, reward, done, info = env.step(action)
    env.render()
