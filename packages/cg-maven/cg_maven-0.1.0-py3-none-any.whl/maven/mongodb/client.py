"""Module that handles the connection to the mongodb."""
import logging
from logging import Logger

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

from maven.exceptions.exceptions import DatabaseConnectionError
from maven.mongodb.config import Config

LOG: Logger = logging.getLogger(__name__)


def get_client(config: Config) -> MongoClient:
    """
    Get a connection to the database.
    Raises:
        ConnectionError if no connection can be established.
    """
    client = MongoClient(
        host=config.uri, serverSelectionTimeoutMS=config.timeout, document_class=dict
    )
    try:
        client.server_info()
        LOG.info("Connected to database.")

    except (
        ServerSelectionTimeoutError,
        ConnectionFailure,
    ) as error:
        LOG.info(f"Database connection error: {error}")
        raise DatabaseConnectionError
    return client


def get_database(client: MongoClient) -> Database:
    """Get the maven database from the MongoClient."""
    return client.get_database(name="maven")
