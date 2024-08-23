#!/bin/env python
# -*- coding: utf-8 -*-

import json

import typer
from rich.console import Console

import vassar.database as db
from vassar.llm import gen_cypher_query

console = Console()
err_console = Console(stderr=True)
app = typer.Typer()


# @app.command()
# def database_schema():
#     schema_json = db.database_schema()
#     console.print_json(schema_json)
#     return schema_json


@app.command()
def adhoc_query(natural_language_query: str = "Who are the children of Mary Doe?"):
    schema_json = db.database_schema()
    query_str = f"""
    Given the following Neo4j database schema

    {schema_json}

    generate a Cypher query that matches the following natural language query:

    {natural_language_query}
    """
    cypher_query = gen_cypher_query(query_str)
    driver = db.get_driver()
    result = db.query(driver, cypher_query)
    console.print(result)
    return result


if __name__ == "__main__":
    app()
