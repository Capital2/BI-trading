from fastapi import APIRouter, Depends, Security, status, Response
from ..models.market_activity_cube import MarketActivityCube
from utilities.dependencies import get_market_activity_cube
from ..schemas.market_activity_forecast import MarketActivityForecastRequest, MarketActivityForecastResponse
from ..controllers.cube_controller import cube_controller

router = APIRouter(
    prefix='/oplap',
    tags=['OLAP']
)

@router.get('/cube_details')
async def cube_details(cube: MarketActivityCube = Depends(get_market_activity_cube)):
    response = {
        "hierarchies": cube.hierarchies._repr_json_(),
        "measures": cube.measures._repr_json_(),
        "levels": cube.levels._repr_json_(),
    }
    
    return response
    
    
@router.get('/market_activity_forecast/{days}/{initial_balance}/{share}')
async def market_activity_forecast(days: int, initial_balance: float, share: str, cube: MarketActivityCube = Depends(get_market_activity_cube)):    
    agent_data = cube_controller.prepare_agent_data(cube_controller.extract_share_data(cube=cube, share=share))
    response = {
        "test": True
    }
    
    return response
