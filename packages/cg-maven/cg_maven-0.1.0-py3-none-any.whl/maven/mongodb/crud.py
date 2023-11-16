"""Base handler for the Maven database."""

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from maven.models.case import Case
from maven.mongodb.client import get_client, get_database
from maven.mongodb.config import Config, connection_config


class CrudHandler:
    def __init__(self, config: Config = connection_config):
        self.config: Config = config
        self.maven_client: MongoClient = get_client(self.config)
        self.maven_db: Database = get_database(self.maven_client)

    def create_collection(self, name: str) -> Collection:
        """Create a collection in the database."""
        return self.maven_db.create_collection(name=name)

    def create_case(self, case: Case):
        """Create a case document in the database."""
        case_json = case.model_dump()
        self.maven_db.case.insert_one(document=case_json)
