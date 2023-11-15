from fastapi import APIRouter, Depends, Security, status, Response
from ..models.market_activity_cube import MarketActivityCube
from utilities.dependencies import get_market_activity_cube

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
    
