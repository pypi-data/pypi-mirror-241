"""Config file to connect to the database."""
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # Connects to localhost change later to vm mongodb
    uri: str = "mongodb://localhost:27017/"
    db_name: str = "maven"
    timeout: int = 30_000  # 30 seconds (default)


connection_config = Config()
