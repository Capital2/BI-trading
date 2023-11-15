from .setup import app
from modules.OLAP.models.market_activity_cube import MarketActivityCube


@app.on_event("startup")
async def startup_event():
    # Creating our singleton instance of the MarketActivityCube class
    app.state.market_activity_cube = MarketActivityCube()
