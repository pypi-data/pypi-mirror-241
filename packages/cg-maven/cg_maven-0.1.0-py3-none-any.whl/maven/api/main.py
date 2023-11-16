import logging

from fastapi import FastAPI

from maven.api.routes import router
from maven.mongodb.client import get_client
from maven.mongodb.config import Config, connection_config

app = FastAPI()
app.include_router(router)
LOG = logging.getLogger("__name__")


@app.on_event("startup")
def startup_db_client(config: Config = connection_config):
    app.mongodb_client = get_client(config)


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
