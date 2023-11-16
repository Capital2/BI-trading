from setup import app
from modules.OLAP.models.market_activity_cube import MarketActivityCube
from modules.Agents.models.manager import Manager

def get_market_activity_cube() -> MarketActivityCube:
    return app.state.market_activity_cube

def get_manager() -> Manager:
    return app.state.manager