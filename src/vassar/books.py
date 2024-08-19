from fasthtml.components import Nav, Header, A, Link, Head, Title, Script, Div, Main
from fasthtml.fastapp import fast_app, serve
from starlette.responses import FileResponse, JSONResponse

from vassar.database import get_neo4j_conn

STANDALONE_KEY = "Standalone"
CHILDREN_KEY = "children"
NAME_KEY = "name"
GRAPH_DATA_QUERY = """
    MATCH (a:Author)-[:WROTE]->(b:Book)
    OPTIONAL MATCH (b)-[:BELONGS_TO]->(s:Series)
    RETURN a.name AS author, b.title AS book, s.name AS series
    """

app, route = fast_app(
    debug=True,
    live=True,
)


@route("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


@route("/graph-data")
async def get(request):  # Query Neo4j database for authors and books
    neo4j_conn = get_neo4j_conn()
    data = neo4j_conn.query(GRAPH_DATA_QUERY)
    root = await format_graph_data(data)
    return JSONResponse(root)


async def format_graph_data(data):
    authors = {}

    for record in data:
        author = record["author"]
        book = record["book"]
        series = record["series"] or STANDALONE_KEY

        if author not in authors:
            authors[author] = {NAME_KEY: author, CHILDREN_KEY: []}

        # Check if the series exists under this author
        series_node = next((item for item in authors[author][CHILDREN_KEY] if item[NAME_KEY] == series), None)

        if not series_node:
            series_node = {NAME_KEY: series, CHILDREN_KEY: []}
            authors[author][CHILDREN_KEY].append(series_node)

        # Add the book under the series
        series_node[CHILDREN_KEY].append({NAME_KEY: book})

    root = {NAME_KEY: "Library", CHILDREN_KEY: list(authors.values())}
    return root


@route("/")
async def get(request):
    # Generate the HTML content using FastHTML
    return (Title("Books and Authors Graph"),
            Head(Link(rel="stylesheet",
                      href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
                      type="text/css"),
                 Link(rel="stylesheet", href="/public/css/styles.css", type="text/css")),
            Main(Header(Nav(
                A("Graph DB Fundamentals", href="/", cls="link dim white b f6 f5-ns dib mr3"),
                A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),
                cls="pa3 pa4-ns"), cls='bg-purple'),
                Div(Div(id="graph", cls="mt4"),
                    cls="center")),
            Script(src="https://d3js.org/d3.v6.min.js"),
            Script(src="/public/js/graph.js"))


if __name__ == "__main__":
    serve(port=8000, reload=True)
