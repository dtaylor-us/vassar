"""
This module provides functions for connecting to a Neo4j database and executing queries.

The following environment variables must be set:
- NEO4J_URI: The URI of the Neo4j database
- NEO4J_USER: The username for the Neo4j database
- NEO4J_PASSWORD: The password for the Neo4j database
"""

import json
import os

from neo4j import (
    AsyncGraphDatabase,
    GraphDatabase,
    Driver,
    AsyncDriver,
    EagerResult,
)

from crud import console


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
    console.log(f"EXECUTING_QUERY:::: {query}")
    records = driver.execute_query(query)
    return records


async def async_query(driver: AsyncDriver, query: str) -> EagerResult:
    console.log(f"EXECUTING_QUERY:::: {query}")
    results = await driver.execute_query(query)
    return results


SCHEMA_QUERY = """
CALL db.schema.nodeTypeProperties() 
YIELD nodeType, nodeLabels, propertyName, propertyTypes, mandatory 
RETURN collect({
    type: nodeType,
    labels: nodeLabels,
    name: propertyName,
    type: propertyTypes,
    mandatory: mandatory
}) AS schema
"""

NODE_QUERY = """
CALL db.schema.nodeTypeProperties() 
YIELD nodeType, nodeLabels, propertyName, propertyTypes, mandatory 
RETURN collect({
    type: nodeType,
    labels: nodeLabels,
    name: propertyName,
    type: propertyTypes,
    mandatory: mandatory
}) AS nodes_schema
"""

RELATIONSHIP_QUERY = """
MATCH ()-[r]->() 
RETURN type(r) AS relationship_type, keys(r) AS properties 
LIMIT 100  // Adjust as needed to avoid performance issue
"""


def database_schema():
    driver = get_driver()
    node_result = query(driver, NODE_QUERY)
    relationship_result = query(driver, RELATIONSHIP_QUERY)
    nodes = node_result.records[0][0]
    relationships = relationship_result.records[0][0]
    schema = dict(nodes=nodes, relationships=relationships)
    schema_json = json.dumps(schema, indent=4)
    return schema_json


async def async_database_schema():
    driver = get_async_driver()
    node_result = await query(driver, NODE_QUERY)
    relationship_result = await query(driver, RELATIONSHIP_QUERY)
    nodes = node_result.records[0][0]
    relationships = relationship_result.records[0][0]
    schema = dict(nodes=nodes, relationships=relationships)
    schema_json = json.dumps(schema, indent=4)
    return schema_json


# def database_schema():
#     driver = get_driver()
#     result = query(
#         driver,
#         SCHEMA_QUERY,
#     )
#     schema = result.records[0][0]
#     schema_json = json.dumps(schema, indent=4)
#     return schema_json

# async def async_database_schema():
#     driver = get_async_driver()
#     result = await async_query(
#         driver,
#         SCHEMA_QUERY,
#     )
#     schema = result.records[0][0]
#     schema_json = json.dumps(schema, indent=4)
#     return schema_json
