"""Base handler for the Maven database."""

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from maven.maven_db.client_connection import get_client, get_database
from maven.maven_db.config import Config, connection_config


class MavenAdapter:
    def __init__(self, config: Config = connection_config):
        self.config: Config = config
        self.maven_client: MongoClient = get_client(self.config)
        self.maven_db: Database = get_database(self.maven_client)
        self.case_collection: Collection = self.maven_db.case


def get_maven_adapter():
    return MavenAdapter(connection_config)
