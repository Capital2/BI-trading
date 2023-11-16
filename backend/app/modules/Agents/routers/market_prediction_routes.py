from fastapi import APIRouter, Depends, Security, status, Response
from utilities.dependencies import get_manager
from ..models.manager import Manager

router = APIRouter(
    prefix='/prediction',
    tags=['Market Prediction']
)

    
@router.get('/market_activity_forecast/{days}/{initial_balance}/{share}')
async def market_activity_forecast(days: int, initial_balance: float, share: str, manager: Manager = Depends(get_manager)):    
    prediction = manager.masters[share].step(initial_balance, days)
    response = {
        "prediction": prediction
    }
    
    return response