import atoti as tt
from utilities.singleton_meta import SingletonMeta
from settings.settings import settings


class MarketActivityCube(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.session = tt.Session()
        self.table = None
        self.cube = None
        self.hierarchies = None
        self.measures = None
        self.levels = None

    def get_table(self):
        db_host = settings.db_host
        db_port = settings.db_port
        db_username = settings.db_username
        db_password = settings.db_password
        db_name = settings.db_name
        self.table = self.session.read_sql(
            "select * from market_activity;",
            url=f"postgresql://{db_host}:{db_port}/{db_name}?user={db_username}&password={db_password}",
            table_name="market_activity",
            keys=["id"],
        )

        print(self.table.head())
        print(type(self.table))

    def create_cube(self):
        self.cube = self.session.create_cube(self.table, "MarketActivityCube")
        self.hierarchies = self.cube.hierarchies
        self.measures = self.cube.measures
        self.levels = self.cube.levels

