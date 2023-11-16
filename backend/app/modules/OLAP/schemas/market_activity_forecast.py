from pydantic import BaseModel

class MarketActivityForecastRequest(BaseModel):
    days: int
    initial_balance: float

class MarketActivityForecastResponse():
    res: 'test'