from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_username: str
    db_password: str
    db_name: str


settings = Settings()
