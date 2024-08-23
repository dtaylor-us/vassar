import os
import csv
from neo4j import GraphDatabase
from dotenv import load_dotenv

class Neo4jLoader:
    def __init__(self, uri, user, password, database):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database

    def close(self):
        self.driver.close()

    def load_csv_to_neo4j(self, file_path, query):
        with self.driver.session(database=self.database) as session:
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    session.run(query, **row)
                print(f"Loaded data from {file_path}")

if __name__ == "__main__":
    load_dotenv()
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_user = os.getenv("NEO4J_USER")
    neo4j_password = os.getenv("NEO4J_PASSWORD")
    neo4j_database = os.getenv("NEO4J_DATABASE", "neo4j")

    loader = Neo4jLoader(neo4j_uri, neo4j_user, neo4j_password, neo4j_database)

    # Example: Load authors data
    loader.load_csv_to_neo4j(
        "data/books/authors.csv",
        "CREATE (:Author {name: $name})"
    )

    # Example: Load books data
    loader.load_csv_to_neo4j(
        "data/books/books.csv",
        "CREATE (:Book {title: $title, published: $published})"
    )

    # Add more data loading logic here

    loader.close()
