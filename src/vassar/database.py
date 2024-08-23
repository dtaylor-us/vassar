"""
This module provides functions for connecting to a Neo4j database and executing queries.

The following environment variables must be set:
- NEO4J_URI: The URI of the Neo4j database
- NEO4J_USER: The username for the Neo4j database
- NEO4J_PASSWORD: The password for the Neo4j database
"""

import os

from neo4j import (
    AsyncGraphDatabase,
    GraphDatabase,
    Driver,
    AsyncDriver,
    EagerResult,
)


# /path/to/project/.envrc
# Contents:
# export NEO4J_URI=bolt://localhost:7687
# export NEO4J_USER=neo4j
# export NEO4J_PASSWORD=neo4j
# export NEO4J_DATABASE=neo4j
#
# From inside the project directory, run:
# $ direnv allow
# $ direnv edit


def get_driver(database: str = None) -> Driver:
    database = database or os.getenv("NEO4J_DATABASE")
    uri = os.getenv("NEO4J_URI")
    auth = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
    return GraphDatabase.driver(uri=uri, auth=auth, database=database)


def get_async_driver(database: str = None) -> AsyncDriver:
    database = database or os.getenv("NEO4J_DATABASE")
    uri = os.getenv("NEO4J_URI")
    auth = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
    return AsyncGraphDatabase.driver(uri=uri, auth=auth, database=database)


def query(driver: Driver, query: str) -> EagerResult:
    records = driver.execute_query(query)
    return records


async def async_query(driver: AsyncDriver, query: str) -> EagerResult:
    results = await driver.execute_query(query)
    return results
