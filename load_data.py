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
                    # Convert string values to appropriate types
                    for key, value in row.items():
                        if key in ['publication_year', 'book_number']:
                            row[key] = int(value) if value else None
                        elif key == 'contribution_percentage':
                            row[key] = float(value) if value else None
                    session.run(query, **row)
                print(f"Loaded data from {file_path}")


if __name__ == "__main__":
    load_dotenv()
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_user = os.getenv("NEO4J_USER")
    neo4j_password = os.getenv("NEO4J_PASSWORD")
    neo4j_database = os.getenv("NEO4J_DATABASE", "neo4j")

    loader = Neo4jLoader(neo4j_uri, neo4j_user, neo4j_password, neo4j_database)
    # Load series data
    loader.load_csv_to_neo4j(
        "n4jdb/import/books/series.csv",
        "CREATE (:Series {series_id: $series_id, name: $name})"
    )

    # Load authors data
    loader.load_csv_to_neo4j(
        "n4jdb/import/books/authors.csv",
        "CREATE (:Author {author_id: $author_id, name: $name, birthdate: $birthdate, nationality: $nationality})"
    )

    # Load books data
    loader.load_csv_to_neo4j(
        "n4jdb/import/books/books.csv",
        "CREATE (:Book {book_id: $book_id, title: $title, publication_year: $publication_year, ISBN: $ISBN, genre: $genre})"
    )

    # Load wrote relationship data
    loader.load_csv_to_neo4j(
        "n4jdb/import/books/wrote_relationship.csv",
        "MATCH (a:Author {author_id: $author_id}), (b:Book {book_id: $book_id}) CREATE (a)-[:WROTE {role: $role, contribution_percentage: $contribution_percentage}]->(b)"
    )

    # Load belongs to series data
    loader.load_csv_to_neo4j(
        "n4jdb/import/books/belongs_to_series.csv",
        "MATCH (b:Book {book_id: $book_id}), (s:Series {series_id: $series_id}) CREATE (b)-[:BELONGS_TO {book_number: $book_number}]->(s)"
    )

    # Add more data loading logic here
    loader.load_csv_to_neo4j(
        "n4jdb/import/vassar/person.csv",
        "CREATE (:Person {person_id: toInteger($person_id), name: $name, birthdate: date($birthdate), gender: $gender, birthplace: $birthplace})")

    loader.load_csv_to_neo4j(
        "n4jdb/import/vassar/relationships.csv",
        "MATCH (parent:Person {person_id: toInteger($parent_id)}), (child:Person {person_id: toInteger($child_id)}) CREATE (parent)-[:PARENT_OF]->(child)")
    loader.close()
