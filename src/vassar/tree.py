from fasthtml.common import *

from vassar.database import get_neo4j_conn

app, rt = fast_app(live=True, debug=True)

GRAPH_DATA_QUERY = """
MATCH (p:Person)-[:PARENT_OF]->(descendant:Person)
RETURN p, descendant;
"""



@rt("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


async def format_graph_data(data):
    nodes = {}
    for record in data:
        parent = record["p"]
        descendant = record["descendant"]

        # Ensure parent node exists
        if parent["name"] not in nodes:
            nodes[parent["name"]] = {"name": parent["name"], "children": []}

        # Ensure descendant node exists
        if descendant["name"] not in nodes:
            nodes[descendant["name"]] = {"name": descendant["name"], "children": []}

        # Append the descendant to the parent's children
        nodes[parent["name"]]["children"].append(nodes[descendant["name"]])

    # Find the root nodes (nodes without parents)
    root_candidates = set(nodes.keys()) - {record["descendant"]["name"] for record in data}
    roots = [nodes[name] for name in root_candidates]

    # If there's only one root, return it; otherwise, create a single root node for all
    if len(roots) == 1:
        return roots[0]
    else:
        return {"name": "Family Tree", "children": roots}


@rt("/tree")
async def get(request):
    neo4j_conn = get_neo4j_conn()
    data = neo4j_conn.query(GRAPH_DATA_QUERY)
    root = await format_graph_data(data)
    return JSONResponse(root)


@rt('/')
def get(): return (Title("Family Tree Visualization"),
                   Head(Link(rel="stylesheet",
                             href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
                             type="text/css")),
                   Nav(A("Graph DB Fundamentals", href="/", cls="link dim white b f6 f5-ns dib mr3"),
                       A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),
                       cls="pa3 pa4-ns"),
                   Main(Div(id="family-tree"), cls="container"),
                   Script(src="https://d3js.org/d3.v6.min.js"),
                   Script(src="/public/js/tree.js"))
