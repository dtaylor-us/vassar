from fasthtml.components import Style, Html, Head, Title, Script, Body, Div
from fasthtml.fastapp import fast_app, serve
from starlette.responses import FileResponse

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


@route("/")
async def get(request):
    # Query Neo4j database for authors and books
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

    # Generate the HTML content using FastHTML
    return Html(
        Head(
            Title("Books and Authors Graph"),
        ),
        Body(
            Div(id="graph"),
            Script(src="https://d3js.org/d3.v6.min.js"),
            Script(type="application/json", id="graph-data")(
                {"nodes": nodes, "links": links}
            ),
            # Script(src="/public/js/graph.js"), # Use either this line or the next line
            GraphJS(),  # This one loads the javascript inlined in the page from this function
        ),
    )


def GraphJS():
    src = """
    document.addEventListener("DOMContentLoaded", function() {
  const data = JSON.parse(document.getElementById("graph-data").textContent);

  const width = 800, height = 600;

  const svg = d3.select("#graph").append("svg")
                .attr("width", width)
                .attr("height", height);

  const simulation = d3.forceSimulation(data.nodes)
                       .force("link", d3.forceLink(data.links).id(d => d.id))
                       .force("charge", d3.forceManyBody())
                       .force("center", d3.forceCenter(width / 2, height / 2));

  const link = svg.append("g")
                  .attr("stroke", "#999")
                  .attr("stroke-opacity", 0.6)
                  .selectAll("line")
                  .data(data.links)
                  .join("line")
                  .attr("stroke-width", d => Math.sqrt(d.value));

  const node = svg.append("g")
                  .attr("stroke", "#fff")
                  .attr("stroke-width", 1.5)
                  .selectAll("circle")
                  .data(data.nodes)
                  .join("circle")
                  .attr("r", 5)
                  .attr("fill", d => d.group === 1 ? "#ff5722" : "#03a9f4")
                  .call(drag(simulation));

  node.append("title")
      .text(d => d.id);

  simulation.on("tick", () => {
      link.attr("x1", d => d.source.x)
          .attr("y1", d => d.source.y)
          .attr("x2", d => d.target.x)
          .attr("y2", d => d.target.y);

      node.attr("cx", d => d.x)
          .attr("cy", d => d.y);
  });

  function drag(simulation) {
      function dragstarted(event, d) {
          if (!event.active) simulation.alphaTarget(0.3).restart();
          d.fx = d.x;
          d.fy = d.y;
      }

      function dragged(event, d) {
          d.fx = event.x;
          d.fy = event.y;
      }

      function dragended(event, d) {
          if (!event.active) simulation.alphaTarget(0);
          d.fx = null;
          d.fy = null;
      }

      return d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended);
  }
});
    """
    return Script(
        src, type="module"
    )  # Note that src does not need to be repeated here (src=src)
    # because it is the first argument, and otherwise would set the code to be the src attribute (which should be a URL)


if __name__ == "__main__":
    serve(port=5005, reload=True)
