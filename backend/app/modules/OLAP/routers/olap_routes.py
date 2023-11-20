from fastapi import APIRouter, Depends, Security, status, Response
from ..models.market_activity_cube import MarketActivityCube
from utilities.dependencies import get_market_activity_cube
from ..schemas.market_activity_forecast import MarketActivityForecastRequest, MarketActivityForecastResponse
from ..controllers.cube_controller import cube_controller
import atoti as tt

router = APIRouter(
    prefix='/oplap',
    tags=['OLAP']
)

@router.get('/cube_details')
async def cube_details(cube: MarketActivityCube = Depends(get_market_activity_cube)):
    # Market activity query
    market_activity_query = cube.cube.query(cube.measures["contributors.COUNT"])
    market_activity_query_dict = market_activity_query.to_dict()
    
    # Max per close share per company
    cube.measures["Max_Close"] = tt.agg.max(cube.table["Close"])
    query = cube.cube.query(cube.measures["Max_Close"], levels=[cube.levels["share"]])
    max_share_per_company = query.to_dict()
    
    # Min close share per company
    cube.measures["Min_Close"] = tt.agg.min(cube.table["Close"])
    query = cube.cube.query(cube.measures["Min_Close"], levels=[cube.levels["share"]])
    min_share_per_company = query.to_dict()
    
    # Mean volume per company (calculate interset in that company)
    mean_volume = cube.cube.query(cube.measures["Volume.MEAN"], levels=[cube.levels["share"]])
    mean_volume_dict = mean_volume.to_dict()
    response = {
        "Market_Activity": market_activity_query_dict['contributors.COUNT'][0],
        "Max_Close": max_share_per_company['Max_Close'],
        "Min_Close": min_share_per_company['Min_Close'],
        "Mean_Volume": mean_volume_dict['Volume.MEAN']
    }
    
    return response
    

