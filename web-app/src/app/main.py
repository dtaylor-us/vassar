from app.database import neo4j_conn
from fasthtml.common import *

hdrs = [
    Style('''* body {
            font-family: Arial, sans-serif;
        }
        
        #graph {
            margin: 20px;
            border: 1px solid #ccc;
        }
    '''),  
    ]
app = FastHTML(hdrs=hdrs)

@app.get("/")
async def get_graph():
    # Query Neo4j database for authors and books
    query = """
    MATCH (a:Author)-[:WROTE]->(b:Book)
    RETURN a.name AS author, b.title AS book
    """
    data = neo4j_conn.query(query)
    
    # Prepare data for D3.js visualization
    nodes = [{"id": record["author"], "group": 1} for record in data]
    books = [{"id": record["book"], "group": 2} for record in data]
    nodes.extend(books)
    
    links = [{"source": record["author"], "target": record["book"], "value": 1} for record in data]

    # Generate the HTML content using FastHTML
    return Html(
        Head(
            Title("Books and Authors Graph"),
            Script(src="https://d3js.org/d3.v6.min.js"),
        ),
        Body(
            Div(id="graph"),
            Script(type="application/json", id="graph-data")(
                {"nodes": nodes, "links": links}
            ),
            GraphJS(),
        )
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
    return Script(src=src, type="module")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
