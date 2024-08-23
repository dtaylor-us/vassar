from typing import List

from fasthtml.components import (
    Nav,
    A,
    Link,
    Head,
    Title,
    Script,
    Div,
    Main,
    Span,
    I,
    Ul,
    Li,
    Button, P, H2,
)
from fasthtml.fastapp import fast_app, serve
from neo4j import Record, EagerResult
from starlette.responses import FileResponse, JSONResponse
from rich.console import Console

from vassar.database import async_query, get_async_driver


console = Console()

app, rt = fast_app(live=True, debug=True)

GRAPH_DATA_QUERY = """
MATCH (p:Person)-[:PARENT_OF]->(descendant:Person)
RETURN p, descendant;
"""

DATABASE = "books"


@rt("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


def format_graph_data(data: EagerResult):
    nodes = {}
    for record in data.records:
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
    root_candidates = set(nodes.keys()) - {
        record["descendant"]["name"] for record in data.records
    }
    roots = [nodes[name] for name in root_candidates]

    # If there's only one root, return it; otherwise, create a single root node for all
    if len(roots) == 1:
        return roots[0]
    else:
        return {"name": "Tree", "children": roots}


@rt("/tree")
async def get(request):
    async with get_async_driver() as driver:
        data = await async_query(driver, GRAPH_DATA_QUERY)
        root = format_graph_data(data)
        return JSONResponse(root)


@rt('/')
def get(): return (
    Title("Family Tree Visualization"),
    Head(
        Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
             type="text/css"),
        Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css")
    ),
    Nav(
        A("Graph DB Fundamentals", href="/", cls="link dim white b f6 f5-ns dib mr3"),
        A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),
        cls="pa3 pa4-ns"
    ),
    Main(
        Div(
            Span(I(cls="fas fa-question-circle light-purple mb3"),
                 P("Help", cls="ml2"), cls="flex pointer info-icon"),
            Div(
                Div(Span("close X", cls="close-btn mb2 f6 light-purple pointer"),
                    cls="flex justify-end items-center"),
                Ul(
                    Li("Zoom: Mouse wheel / touchpad scroll"),
                    Li("Pan: Click and drag."),
                    cls="pl3"
                ),
                cls="info-banner bg-navy pa3 ba br-rounded b--light-silver br2 shadow-1 dn"
            ),
            cls="info-container fixed bottom-2 right-2"
        ),
        H2("Family Tree Visualization", cls="tc"),
        Button("Expand All", id="expand-all", cls="f6 link dim br-rounded ph3 pv2 mb4 mt2 dib white bg-dark-blue"),
        Button("Collapse All", id="collapse-all", cls="dn f6 link dim br-rounded ph3 pv2 mb4 mt2  white bg-dark-blue"),
        Div(id="family-tree"),
        cls="container"
    ),

    Script(src="https://d3js.org/d3.v6.min.js"),
    Script(src="/public/js/tree.js")
)


if __name__ == "__main__":
    serve(port=8001, reload=True)
