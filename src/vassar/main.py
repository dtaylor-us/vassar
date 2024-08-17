import json

from fasthtml.components import Nav, Style, Header, A, Html, Link, Head, Title, Script, Body, Div, H1
from fasthtml.fastapp import fast_app, serve
from starlette.responses import FileResponse, JSONResponse

from vassar.database import get_neo4j_conn

app, route = fast_app(
    debug=True,
    live=True,
)


@route("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


@route("/graph-data")
async def get(request):  # Query Neo4j database for authors and books
    query = """
    MATCH (a:Author)-[:WROTE]->(b:Book)
    OPTIONAL MATCH (b)-[:BELONGS_TO_SERIES]->(s:Series)
    RETURN a.name AS author, b.title AS book, s.name AS series
    """
    neo4j_conn = get_neo4j_conn()
    data = neo4j_conn.query(query)

    # Prepare data for D3.js radial tidy tree
    authors = {}
    for record in data:
        author = record["author"]
        book = record["book"]
        series = record["series"]

        if author not in authors:
            authors[author] = {"name": author, "children": []}

        if series:
            # Check if the series exists under this author
            series_node = next(
                (
                    item
                    for item in authors[author]["children"]
                    if item["name"] == series
                ),
                None,
            )
            if not series_node:
                series_node = {"name": series, "children": []}
                authors[author]["children"].append(series_node)
            # Add the book under the series
            series_node["children"].append({"name": book})
        else:
            # Add the book directly under the author
            authors[author]["children"].append({"name": book})

    root = {"name": "Library", "children": list(authors.values())}

    return JSONResponse(root)


@route("/")
async def get(request):
    # Generate the HTML content using FastHTML
    return Html(
        Head(
            Title("Books and Authors Graph"),
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
                type="text/css",
            ),
        ),
        Body(
            Header(Nav(
                A("Site Name", href="/", cls="link dim white b f6 f5-ns dib mr3"),
                A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),
                cls="pa3 pa4-ns"
            ), cls='bg-light-purple'),
            Div(
                Div(id="graph", cls="mt6"),
                cls="center",
            ),
        ),
        Script(src="https://d3js.org/d3.v6.min.js"),
        Script(src="/public/js/graph.js"),
    )


if __name__ == "__main__":
    serve(port=8000, reload=True)
