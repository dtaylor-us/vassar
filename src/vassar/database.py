import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from contextlib import asynccontextmanager


class Neo4jConnection:
    def __init__(self, uri, user, password, database):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self._database = database

    def close(self):
        self._driver.close()

    @asynccontextmanager
    async def session(self):
        session = self._driver.session(database=self._database)
        try:
            yield session
        finally:
            session.close()

    def verify_connection(self):
        try:
            with self._driver.session(database=self._database) as session:
                result = session.run("RETURN 1")
                if result.single()[0] == 1:
                    print("Connection to Neo4j is successful!")
                else:
                    print("Connection to Neo4j failed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def query(self, query, parameters=None):
        with self._driver.session(database=self._database) as session:
            result = session.run(query, parameters)
            return [record for record in result]


def get_neo4j_conn():
    load_dotenv()
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

    # Load and print credentials for debugging
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_user = os.getenv("NEO4J_USER")
    neo4j_password = os.getenv("NEO4J_PASSWORD")
    neo4j_database = os.getenv(
        "NEO4J_DATABASE", "neo4j"
    )  # Default to 'neo4j' if not specified

    print(f"Using Neo4j URI: {neo4j_uri}")
    print(f"Using Neo4j User: {neo4j_user}")
    print(f"Using Neo4j Database: {neo4j_database}")

    neo4j_conn = Neo4jConnection(neo4j_uri, neo4j_user, neo4j_password, neo4j_database)
    # Verify connectivity
    neo4j_conn.verify_connection()

    return neo4j_conn
