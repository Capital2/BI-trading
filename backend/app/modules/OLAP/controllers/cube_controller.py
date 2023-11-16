from ..models.market_activity_cube import MarketActivityCube
from utilities.singleton_meta import SingletonMeta
from pandas import DataFrame

class CubeController(metaclass=SingletonMeta):    
    def extract_share_data(self, cube: MarketActivityCube, share: str) -> DataFrame:        
        query_result = cube.table.query(filter=cube.table["share"] == share)
        return query_result
    
    def prepare_agent_data(self, df: DataFrame):
        df.drop(columns=['name', 'share', 'id'], inplace=True)
        df.set_index('date', inplace=True)
        print("df input to the agent")
        print(df.head())
        
        return df
        
        
cube_controller = CubeController()