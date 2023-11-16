from utilities.singleton_meta import SingletonMeta
from .agent_SMA import SimpleMovingAverageAgent
from .agent_RSI import RSITradingAgent
from .agent_MACD import MACDTradingAgent
from .agent_OBV import OBVTradingAgent
from .agent_price_predictor import PricePredictionAgent
from .agent_Master import MasterTradingAgent
from modules.OLAP.controllers.cube_controller import cube_controller
from modules.OLAP.models.market_activity_cube import MarketActivityCube
from multiprocessing import Process


class Manager(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.shares = ["ACCO", "FISB", "ATNFW", "GME", "ASCBR"]
        self.masters = {}

        self.init_masters()

    def init_master(self):
        pass

    # def init_masters(self):
    #     processes = [None] * 5
    #     for i in range(0, len(self.shares)):
    #         df = cube_controller.prepare_agent_data(
    #             cube_controller.extract_share_data(MarketActivityCube(), self.shares[i])
    #         )

    #         sma_agent = SimpleMovingAverageAgent(df, self.shares[i])
    #         obv_agent = OBVTradingAgent(df, self.shares[i])
    #         rsi_agent = RSITradingAgent(df, self.shares[i])
    #         macd_agent = MACDTradingAgent(df, self.shares[i])

    #         self.masters[self.shares[i]] = MasterTradingAgent(
    #             sma_agent, rsi_agent, obv_agent, macd_agent
    #         )
    #         processes[i] = Process(target=self.masters[self.shares[i]].train_models)
    #         processes[i].start()

    #     for process in processes:
    #         process.join()
            
    #     print("All models trained")
    #     print(self.masters)
    
    def init_masters(self):
        for i in range(0, len(self.shares)):
            df = cube_controller.prepare_agent_data(
                cube_controller.extract_share_data(MarketActivityCube(), self.shares[i])
            )

            sma_agent = SimpleMovingAverageAgent(df, self.shares[i])
            obv_agent = OBVTradingAgent(df, self.shares[i])
            rsi_agent = RSITradingAgent(df, self.shares[i])
            macd_agent = MACDTradingAgent(df, self.shares[i])
            predictor = PricePredictionAgent(df, self.shares[i])

            self.masters[self.shares[i]] = MasterTradingAgent(
                sma_agent, rsi_agent, obv_agent, macd_agent, predictor
            )
            
            self.masters[self.shares[i]].train_models()
            print("Model trained for " + self.shares[i])
            
        print("All models trained")
        print(self.masters)
