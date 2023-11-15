from ..setup import app
from modules.OLAP.models.market_activity_cube import MarketActivityCube

def get_market_activity_cube() -> MarketActivityCube:
    return app.state.market_activity_cube