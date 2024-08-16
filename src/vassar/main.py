import json

from fasthtml.components import Style, Html, Head, Title, Script, Body, Div, ScriptX
from fasthtml.fastapp import fast_app, serve
from starlette.responses import FileResponse, JSONResponse

from vassar.database import get_neo4j_conn

app, route = fast_app(
    debug=True,
    live=True,
    hdrs=(
        Style("""* body {
                    font-family: Arial, sans-serif;
                }

                #graph {
                    margin: 20px;
                    border: 1px solid #ccc;
                }
            """),
    ),
)


@route("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")

@route("/graph-data")
async def get(request):    # Query Neo4j database for authors and books
    query = """
    MATCH (a:Author)-[:WROTE]->(b:Book)
    RETURN a.name AS author, b.title AS book
    """
    neo4j_conn = get_neo4j_conn()
    data = neo4j_conn.query(query)

    # Prepare data for D3.js visualization
    nodes = [{"id": record["author"], "group": 1} for record in data]
    books = [{"id": record["book"], "group": 2} for record in data]
    nodes.extend(books)

    links = [
        {"source": record["author"], "target": record["book"], "value": 1}
        for record in data
    ]
    # nodes = []
    # links = []

    return JSONResponse({"nodes": nodes, "links": links})


@route("/")
async def get(request):
    # Generate the HTML content using FastHTML
    return Html(
        Head(
            Title("Books and Authors Graph"),
        ),
        Body(
            Div(id="graph"),
            Script(src="https://d3js.org/d3.v6.min.js"),
            Script(src="/public/js/graph.js")
        ),
    )

if __name__ == "__main__":
    serve(port=8000, reload=True)
