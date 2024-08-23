# Fundamentals of working with Graph Databases

## Introduction

**What is a Graph Database?**
A graph database is a type of NoSQL database that models data in a graph format, using nodes, edges (relationships), and
properties. Unlike traditional relational databases that use tables, graph databases are designed to highlight the
relationships between data points, making them ideal for complex queries and analyses where connections between entities
are important.

**Recommendation Engines:**
Companies like Amazon and Netflix use graph databases to analyze user behavior and recommend products or content based
on patterns of similarity and shared interests among users.

**Fraud Detection:**
Financial institutions use graph databases to detect fraudulent activity by analyzing transactions and identifying
suspicious patterns that may indicate money laundering or other illegal activities.

**Knowledge Graphs:**
Google’s Knowledge Graph organizes information from the web into a comprehensive, connected understanding of facts and
concepts, improving search results and information retrieval.

**Examples:**

- 🎬 [Neo4j Movie Graph](https://neo4j.com/graph-examples/)
- 🕵️‍♂️ [Explore the Panama Papers Graph](https://panamapapers.icij.org/graphs/)
- 📚 [Wikidata Query Service](https://query.wikidata.org/)
- 🌐 [YAGO Knowledge Graph](https://yago-knowledge.org/)
- 📖 [DBpedia SPARQL Endpoint](https://dbpedia.org/sparql)
- 🛠️ [Amazon Neptune Demos](https://aws.amazon.com/neptune/getting-started/)

#### **Graph Elements**

**Nodes (Vertices):**
Represent entities such as people, products, or concepts. In our "Books and Authors" example, nodes would
represent `Authors` and `Books`.

**Relationships (Edges):**
Represent the connections between nodes, showing how they are related. For instance, an `Author` node might have
a `WROTE` relationship connecting it to a `Book` node.

**Labels:**
Labels are used to categorize nodes and relationships in a graph. For instance, a node might be labeled as `Author`
or `Book`. Labels help in querying the graph by filtering nodes or relationships of interest.

**Properties:**
Each node or relationship can store properties. For example, an `Author` node could have properties
like `name`, `birthdate`, and `nationality`. These properties provide detailed information that can be used in queries
to filter results or retrieve specific data.

#### **Directed and Undirected Graphs**

**Node Traversal:**
In a directed graph, edges have a direction, indicating a one-way relationship between nodes. Traversal in a graph
involves moving from one node to another along these directed edges. For example, in the "Books and Authors" graph, you
can traverse from an `Author` to the `Books` they wrote by following the `WROTE` relationship.

In contrast, an undirected graph does not have a direction associated with its edges. Traversal in an undirected graph
allows movement between nodes in both directions. For example, in the "Books and Authors" graph, you can traverse from
an `Author` to the `Books` they wrote and vice versa, as the relationship is not one-way.

**Characteristics:**
Directed graphs are used when the relationship between nodes has a clear direction, such as parent-child relationships,
dependencies, or sequences. This is crucial in understanding hierarchies or flow processes.

Undirected graphs, on the other hand, are used when the relationship between nodes is bidirectional or does not have a
specific direction. This is useful for modeling relationships where the direction is not important, such as friendships
or collaborations between authors.

#### **Weighted and Unweighted Graphs**

**Edge Weights:**
In a weighted graph, edges have a numerical value associated with them, known as the weight. This weight represents the
strength, distance, or cost of the relationship between nodes. For example, in the "Books and Authors" graph, you can
assign a weight to the `WROTE` relationship to indicate the significance or popularity of a book.

In contrast, an unweighted graph does not assign any numerical value to its edges. The relationships between nodes are
considered to have equal importance or cost. For example, in the "Books and Authors" graph, you can represent
the `WROTE` relationship as unweighted if the importance or popularity of books is not a factor in your analysis.

**Characteristics:**
Weighted graphs are used when the strength or importance of the relationship between nodes needs to be considered. This
is useful for various applications, such as finding the shortest path between nodes based on the least weighted edges or
determining the most influential nodes in a network.

Unweighted graphs, on the other hand, are used when the relationships between nodes are considered to have equal
importance or when the focus is on the structure of the graph rather than the specific weights of the edges.

#### **Performance Advantage over RDBMS**

In a relational database, retrieving connected data often requires expensive join operations between tables, which can
become slow as data grows. In a graph database, each node directly references its adjacent nodes through relationships,
allowing for fast and efficient traversals without needing to perform joins. This is known as index-free adjacency and
is one of the key advantages of graph databases, especially for queries that require traversing multiple levels of
connections.

### Getting Started with Neo4j

There are several ways to get started with Neo4j:

#### Neo4j Aura

Neo4j Aura is a fully-managed cloud service provided by Neo4j. It's the simplest way to run Neo4j in the cloud,
completely automated and fully managed. It's always on and ideal for building cloud-based applications with graph
technology.

To get started with Neo4j Aura:

1. Visit the [Neo4j Aura](https://neo4j.com/cloud/aura/) website.
2. Click on `Start Free` or `Login` if you already have an account.
3. Once logged in, you can create a new database by clicking on `Create Database`.
4. Follow the instructions to configure your database and click `Create`.
5. Once your database is ready, you can connect to it using the provided connection details.

#### Neo4j Desktop

Neo4j Desktop is an application environment that allows you to design, develop, and deploy graph applications right from
your local machine. It's ideal for local development and testing.

To get started with Neo4j Desktop:

1. Download Neo4j Desktop from the [Neo4j Download Center](https://neo4j.com/download/).
2. Install the application on your machine.
3. Open Neo4j Desktop and create a new Project.
4. Inside the project, click on `Add` and then `Local DBMS`.
5. Configure your database and click `Create`.
6. Once your database is ready, you can start it by clicking on `Start`.

#### Docker

If you prefer to use Docker for managing your development environments, you can use the official Neo4j Docker image.

To get started with Neo4j on Docker:

1. Ensure you have Docker installed on your machine. If not, you can download it from
   the [Docker website](https://www.docker.com/products/docker-desktop).
2. Pull the Neo4j image from Docker Hub by running the following command in your terminal:

```bash
docker pull neo4j
```

3. Once the image is pulled, you can start a Neo4j container with the following command:

```bash
docker run \
    --name testneo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -e NEO4J_AUTH=neo4j/test \
    neo4j
```

In this command, replace `$HOME/neo4j/data` and `$HOME/neo4j/logs` with the paths where you want to store your data and
logs. Replace `neo4j/test` with the username and password you want to use for your database.

4. You can then access the Neo4j Browser at `http://localhost:7474` and connect to your database using the credentials
   you provided.

#### Introduction to Cypher

**Cypher Query Language:**
Cypher is a powerful, expressive query language designed specifically for querying and manipulating graph databases. It
allows you to describe patterns in your data graphically, making it intuitive to write queries.

##### Basic Structure of Cypher Query

A Cypher query consists of several components:

1. **MATCH:** This keyword is used to specify the pattern of nodes and relationships to match in the graph.

2. **Nodes and Relationships:** Nodes are represented by parentheses, and relationships are represented by hyphens. The
   direction of the relationship can be specified using arrows (-> for outgoing, <- for incoming, and -- for
   bidirectional).

3. **Labels and Properties:** Labels are used to categorize nodes, and properties are key-value pairs that provide
   additional information about nodes and relationships.

4. **RETURN:** This keyword is used to specify the data to be returned as the result of the query.

Here's an example of a basic Cypher query structure:

```cypher
MATCH (a:Label1)-[:RELATIONSHIP]->(b:Label2)
RETURN a.property1, b.property2
```

In this example, the query matches nodes labeled as "Label1" connected to nodes labeled as "Label2" via a "RELATIONSHIP"
relationship. The query then returns the values of "property1" from node "a" and "property2" from node "b".

Remember to replace "Label1", "Label2", "RELATIONSHIP", "property1", and "property2" with the actual labels and
properties relevant to your graph database.

**Example: Finding Specific Authors**

This query matches an `Author` node with the name "J.K. Rowling" and retrieves the connected `Book` nodes via
the `WROTE` relationship. The `RETURN` statement specifies that we want to see the book's title, publication year, and
genre.

```cypher
MATCH (a:Author {name: "J.K. Rowling"})-[:WROTE]->(b:Book)
RETURN b.title, b.publication_year, b.genre
```

#### Creating Nodes

**Creating a Node:**
This command creates a new `Author` node with the specified properties. Discuss how Cypher uses the `CREATE` keyword to
add new data to the graph.

```cypher
CREATE (a:Author {name: "George R.R. Martin", birthdate: "1948-09-20", nationality: "American"})
```

**Creating Relationships:**
This query first finds an existing `Author` and `Book`, then creates a `WROTE` relationship between them. The
relationship itself can have properties, such as `role` and `contribution_percentage`, which provide additional context.

```cypher
MATCH (a:Author {name: "George R.R. Martin"}), (b:Book {title: "A Game of Thrones"})
CREATE (a)-[:WROTE {role: "Primary Author", contribution_percentage: 100.0}]->(b)
```

#### Updating Properties

**Adding Properties to a Book:**
This query finds the `Book` node with the title "A Game of Thrones" and adds or updates its `genre` property. Discuss
how the `SET` command is used to modify existing nodes and their properties.

```cypher
MATCH (b:Book {title: "A Game of Thrones"})
SET b.genre = "Fantasy"
```

**Merge Processing:**
`MERGE` is a powerful command that either matches an existing node or creates a new one if it doesn’t exist. This is
useful for avoiding duplicate entries and ensuring data consistency.

```cypher
MERGE (b:Book {title: "A Clash of Kings"})
ON CREATE SET b.publication_year = 1998, b.genre = "Fantasy"
ON MATCH SET b.publication_year = 1998, b.genre = "Fantasy"
```

#### Deleting Data

**Deleting a Relationship:**
This command deletes the specific `WROTE` relationship between the author and the book. Discuss the importance of
managing relationships carefully to maintain data integrity.

```cypher
MATCH (a:Author {name: "J.K. Rowling"})-[r:WROTE]->(b:Book {title: "Harry Potter and the Sorcerer’s Stone"})
DELETE r
```

**Deleting a Node:**
This command deletes a node from the graph. Mention that deleting a node also requires handling any connected
relationships to avoid orphaned data.

```cypher
MATCH (b:Book {title: "A Clash of Kings"})
DELETE b
```

#### Importing Data

Neo4j provides a powerful `LOAD CSV` Cypher command which allows you to import data from CSV files directly into the
graph database.

Here's a basic example of how you can use `LOAD CSV` to import data:

```cypher
LOAD CSV WITH HEADERS FROM 'file:///path/to/your/file.csv' AS row
CREATE (:Label {property1: row.column1, property2: row.column2})
```

In this example, replace Label with the label for the nodes you're creating, property1 and property2 with the property
names, and column1 and column2 with the column names from your CSV file. Please note that the file path in the LOAD CSV
command is relative to the Neo4j import directory. If you're running Neo4j Desktop, this is typically the import
directory inside your Neo4j database folder.

##### **Loading Author and Book Data**

Files for the Author and Book demo can be found in the `data` directory of the project.

```cypher
LOAD CSV WITH HEADERS FROM 'file:///series.csv' AS row
CREATE (:Series {series_id: row.series_id, name: row.name});

LOAD CSV WITH HEADERS FROM 'file:///authors.csv' AS row
CREATE (:Author {author_id: row.author_id, name: row.name, birthdate: row.birthdate, nationality: row.nationality});


LOAD CSV WITH HEADERS FROM 'file:///books.csv' AS row
CREATE (:Book {book_id: row.book_id, title: row.title, publication_year: toInteger(row.publication_year), ISBN: row.ISBN, genre: row.genre});

LOAD CSV WITH HEADERS FROM 'file:///wrote_relationship.csv' AS row
MATCH (a:Author {author_id: row.author_id}), (b:Book {book_id: row.book_id})
CREATE (a)-[:WROTE {role: row.role, contribution_percentage: toFloat(row.contribution_percentage)}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///belongs_to_series.csv' AS row
MATCH (b:Book {book_id: row.book_id}), (s:Series {series_id: row.series_id})
CREATE (b)-[:BELONGS_TO {book_number: toInteger(row.book_number)}]->(s);
```

#### **Loading Person and Relationship Data**

```cypher
// Create uniqueness constraints
CREATE CONSTRAINT FOR (p:Person) REQUIRE p.person_id IS UNIQUE;

// Load persons data
LOAD CSV WITH HEADERS FROM 'file:///persons.csv' AS row
CREATE (:Person {person_id: toInteger(row.person_id), name: row.name, birthdate: date(row.birthdate), gender: row.gender, birthplace: row.birthplace});

// Load parent-child relationships
LOAD CSV WITH HEADERS FROM 'file:///relationships.csv' AS row
MATCH (parent:Person {person_id: toInteger(row.parent_id)}), (child:Person {person_id: toInteger(row.child_id)})
CREATE (parent)-[:PARENT_OF]->(child);
```

### **Building a Web Application with Python Tooling and D3.js**

In this demo, we will provide more detailed setup instructions and implementation guidance for building a web
application that visualizes the relationships between authors and books using Python, FastAPI, Neo4j, FastHTML, and
D3.js. The project will be structured for easy development, using Rye for Python package management and FastHTML for
templating.

---

### **Folder Structure**

We will organize the project in a clear and modular way:

```
web-app/
│
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py        # Neo4j database connection
│   │   ├── main.py            # FastAPI application setup
│   │   └── public/
│   │       └── js/
│   │           └── graph.js   # D3.js code
│   └── tests/
│       ├── __pycache__/
│       │   ├── __init__.cpython-312.pyc
│       │   ├── database.cpython-312.pyc
│       │   └── main.cpython-312.pyc
│       └── test_api.py        # Unit tests for the API
└── .env                       # Environment variables
```

### **Setting Up the Backend with FastAPI**

#### **FastAPI Overview**

FastAPI is a high-performance web framework suitable for building REST APIs. It supports Python type hints, asynchronous
request handling, and automatic generation of OpenAPI docs.

#### **Installing Dependencies with Rye**

Rye is a toolchain for Python that manages packages, virtual environments, and builds.

1. **Create a Rye project:**

   ```bash
   rye init web-app
   ```

2. **Install Uvicorn, Neo4j Driver, and FastHTML:**

   ```bash
   rye add uvicorn\[standard\] neo4j python-fasthtml
   ```

3. **Setup .env File:**
   Create a `.env` file in the project root to store environment variables:
   ```
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=password
   ```

#### **Connecting to the Neo4j Database**

**`database.py`:**

```python
import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from contextlib import asynccontextmanager


class Neo4jConnection:
    def __init__(self, uri, user, password, database):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        self._database = database

    def close(self):
        self._driver.close()

    @asynccontextmanager
    async def session(self):
        session = self._driver.session(database=self._database)
        try:
            yield session
        finally:
            session.close()

    def verify_connection(self):
        try:
            with self._driver.session(database=self._database) as session:
                result = session.run("RETURN 1")
                if result.single()[0] == 1:
                    print("Connection to Neo4j is successful!")
                else:
                    print("Connection to Neo4j failed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def query(self, query, parameters=None):
        with self._driver.session(database=self._database) as session:
            result = session.run(query, parameters)
            return [record for record in result]


def get_neo4j_conn():
    load_dotenv()

    # Load and print credentials for debugging
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_user = os.getenv("NEO4J_USER")
    neo4j_password = os.getenv("NEO4J_PASSWORD")
    neo4j_database = os.getenv(
        "NEO4J_DATABASE", "neo4j"
    )  # Default to 'neo4j' if not specified

    print(f"Using Neo4j URI: {neo4j_uri}")
    print(f"Using Neo4j User: {neo4j_user}")
    print(f"Using Neo4j Database: {neo4j_database}")

    neo4j_conn = Neo4jConnection(neo4j_uri, neo4j_user, neo4j_password, neo4j_database)
    # Verify connectivity
    neo4j_conn.verify_connection()

    return neo4j_conn

```

**`main.py`:**

```python
from fasthtml.components import Nav, Header, A, Html, Link, Head, Title, Script, Body, Div
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
    return Html(
        Head(
            Title("Books and Authors Graph"),
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/tachyons/4.11.1/tachyons.min.css",
                type="text/css",
            ),
            Link(rel="stylesheet", href="/public/css/styles.css", type="text/css"),
        ),
        Body(
            Header(Nav(
                A("Graph DB Fundamentals", href="/", cls="link dim white b f6 f5-ns dib mr3"),
                A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),
                cls="pa3 pa4-ns"
            ), cls='bg-purple'),
            Div(
                Div(id="graph", cls="mt4"),
                cls="center",
            ),
        ),
        Script(src="https://d3js.org/d3.v6.min.js"),
        Script(src="/public/js/graph.js"),
    )


if __name__ == "__main__":
    serve(port=8000, reload=True)

```

#### **Adding D3.js Visualization**

**`static/js/graph.js`:**

```javascript
document.addEventListener("DOMContentLoaded", async () => {
    // Fetch the data from the backend
    const response = await fetch("/graph-data");
    const data = await response.json();

    // Utility function to truncate text
    function truncateText(text, maxLength) {
        return text.length > maxLength ? text.slice(0, maxLength) + '...' : text;
    }

    // Set the dimensions and radius of the sunburst
    const width = 928;
    const height = 928;
    const radius = Math.min(width, height) / 2;

    // Create the partition layout
    const partition = d3.partition()
        .size([2 * Math.PI, radius]);

    // Convert the data into a hierarchy and apply partition layout
    const root = partition(d3.hierarchy(data)
        .sum(d => d.value || 1) // Use value if present, otherwise 1 for equal sizing
        .sort((a, b) => b.value - a.value)
    );

    // Create a color scale based on the root author's children length
    const color = d3.scaleOrdinal(d3.quantize(d3.interpolateRainbow, data.children.length + 1));

    // Create the SVG container centered on the screen
    const svg = d3.select("#graph")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .style("display", "block")
        .style("margin", "0 auto")
        .append("g")
        .attr("transform", `translate(${width / 2},${height / 2})`);

    // Define the arc generator with padding for visual separation
    const arc = d3.arc()
        .startAngle(d => d.x0)
        .endAngle(d => d.x1)
        .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
        .padRadius(radius / 2)
        .innerRadius(d => d.y0)
        .outerRadius(d => d.y1 - 1);

    // Create a tooltip div that is hidden by default
    const tooltip = d3.select("body").append("div")
        .style("position", "absolute")
        .style("visibility", "hidden")
        .style("background", "#fff")
        .style("border", "1px solid #ccc")
        .style("padding", "8px")
        .style("border-radius", "4px")
        .style("box-shadow", "0px 0px 10px rgba(0, 0, 0, 0.1)")
        .style("font-family", "sans-serif")
        .style("font-size", "12px");

    // Draw the arcs (sunburst segments)
    const paths = svg.append("g")
        .attr("fill-opacity", 0.6)
        .selectAll("path")
        .data(root.descendants().filter(d => d.depth))
        .join("path")
        .attr("fill", d => {
            while (d.depth > 1) d = d.parent;
            return color(d.data.name);
        })
        .attr("d", arc)
        .on("mouseover", function (event, d) {
            tooltip.style("visibility", "visible")
                .text(d.data.name); // Display the full text in the tooltip
            d3.select(this).attr("fill-opacity", 1); // Darken the opacity on hover
        })
        .on("mousemove", function (event) {
            tooltip.style("top", (event.pageY - 10) + "px")
                .style("left", (event.pageX + 10) + "px");
        })
        .on("mouseout", function (event, d) {
            tooltip.style("visibility", "hidden");
            d3.select(this).attr("fill-opacity", 0.6); // Reset the opacity after hover
        });

    // Add text labels with truncation and proper rotation and alignment
    svg.append("g")
        .attr("pointer-events", "none")
        .attr("text-anchor", "middle")
        .attr("font-size", 10)
        .attr("font-family", "sans-serif")
        .selectAll("text")
        .data(root.descendants().filter(d => d.depth && (d.y0 + d.y1) / 2 * (d.x1 - d.x0) > 10))
        .join("text")
        .attr("transform", function (d) {
            const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
            const y = (d.y0 + d.y1) / 2;
            return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
        })
        .attr("dy", "0.35em")
        .text(d => truncateText(d.data.name, 15)) // Truncate the text if necessary
        .append("title")
        .text(d => d.data.name); // Ensure full text appears on hover
});
```

#### **Adding Static Files**

**`static/css/style.css`:**

```css
body {
    font-family: Arial, sans-serif;
}

#graph {
    margin: 20px;
    border: 1px solid #ccc;
}
```

### **3. Running the Application**

1. **Start the server using Uvicorn:**

   ```bash
   rye run uvicorn app.books:app --reload
   ```

2. **Access the application in your browser:**
    - Navigate to `http://localhost:8000/` to view the D3.js visualization of the "Books and Authors" graph.
    -

#### **Deploying the Application**

### **Building a Web Application to Visualize a Family Tree with Python Tooling and D3.js**

In this demo, we'll walk through the process of creating a web application that visualizes a family tree using a graph
database schema. The application will allow users to explore the hierarchical relationships within a family, such as
parent-child and sibling relationships. The backend will be powered by FastAPI, and the frontend will use D3.js to
render the family tree.

---

#### **Designing the Family Tree Graph Schema**

**Nodes (Entities):**

**Person**

- `name`: String (e.g., "John Doe")
- `birthdate`: Date (e.g., "1980-01-15")
- `gender`: String (e.g., "Male" or "Female")
- `birthplace`: String (e.g., "New York")

**Relationships:**

**PARENT_OF**

- **From:** Person
- **To:** Person
- **Properties:**
    - `relationship`: String (e.g., "Mother", "Father")

**SIBLING_OF**

- **From:** Person
- **To:** Person
- **Properties:**
    - `relationship`: String (e.g., "Brother", "Sister")

**Example Data:**

Nodes:

- Person: `{name: "John Doe", birthdate: "1980-01-15", gender: "Male", birthplace: "New York"}`
- Person: `{name: "Jane Doe", birthdate: "1978-03-22", gender: "Female", birthplace: "New York"}`
- Person: `{name: "Alice Doe", birthdate: "2005-07-18", gender: "Female", birthplace: "New York"}`

Relationships:

- `(John Doe)-[:PARENT_OF]->(Alice Doe)`
- `(Jane Doe)-[:PARENT_OF]->(Alice Doe)`
- `(John Doe)-[:SIBLING_OF]->(Jane Doe)`

---

#### **Setting Up the Backend with FastHTML**

**FastHTML Application Setup:**

We'll use FastHTML, a Python framework that allows for fast and efficient rendering of HTML in the backend while
interacting with Neo4j.

```python
from fasthtml.fastapp import fast_app, serve
from neo4j import GraphDatabase

app, route = fast_app(debug=True, live=True)

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))


@app.on_event("shutdown")
def shutdown():
    driver.close()


def get_db():
    with driver.session() as session:
        yield session
```

- **API Endpoint for Family Tree:**

Create an endpoint to retrieve the entire family tree starting from a specific person:

```python
@route("/family-tree/{person_name}")
async def get_family_tree(request, person_name: str):
    query = """
    MATCH (p:Person {name: $person_name})-[:PARENT_OF*0..]->(descendants)
    OPTIONAL MATCH (p)-[:SIBLING_OF]->(siblings)
    RETURN p, descendants, siblings
    """
    with driver.session() as session:
        result = session.run(query, person_name=person_name)
        nodes = []
        links = []
        for record in result:
            parent = record["p"]
            nodes.append({"id": parent["name"], "group": 1})
            if "descendants" in record:
                for child in record["descendants"]:
                    nodes.append({"id": child["name"], "group": 2})
                    links.append({"source": parent["name"], "target": child["name"], "value": 1})
            if "siblings" in record:
                for sibling in record["siblings"]:
                    nodes.append({"id": sibling["name"], "group": 3})
                    links.append({"source": parent["name"], "target": sibling["name"], "value": 1})
        return {"nodes": nodes, "links": links}
```

- **Explanation:**
    - This endpoint retrieves all descendants and siblings of a specified person. It returns the family members as nodes
      and the relationships between them as links.

---

#### **Building the Frontend with D3.js**

- **Visualizing the Family Tree:**

Use D3.js to create a hierarchical tree that represents the family structure. Here’s a basic example:

```html

<div id="family-tree"></div>
<script src="https://d3js.org/d3.v6.min.js"></script>
<script>
    fetch("/family-tree/John Doe")
            .then((response) => response.json())
            .then((data) => {
                const width = 800,
                        height = 600;

                const svg = d3
                        .select("#family-tree")
                        .append("svg")
                        .attr("width", width)
                        .attr("height", height);

                const simulation = d3
                        .forceSimulation(data.nodes)
                        .force(
                                "link",
                                d3.forceLink(data.links).id((d) => d.id)
                        )
                        .force("charge", d3.forceManyBody())
                        .force("center", d3.forceCenter(width / 2, height / 2));

                const link = svg
                        .append("g")
                        .attr("stroke", "#999")
                        .attr("stroke-opacity", 0.6)
                        .selectAll("line")
                        .data(data.links)
                        .join("line")
                        .attr("stroke-width", (d) => Math.sqrt(d.value));

                const node = svg
                        .append("g")
                        .attr("stroke", "#fff")
                        .attr("stroke-width", 1.5)
                        .selectAll("circle")
                        .data(data.nodes)
                        .join("circle")
                        .attr("r", 5)
                        .attr("fill", (d) =>
                                d.group === 1 ? "#ff5722" : d.group === 2 ? "#03a9f4" : "#4caf50"
                        )
                        .call(drag(simulation));

                node.append("title").text((d) => d.id);

                simulation.on("tick", () => {
                    link
                            .attr("x1", (d) => d.source.x)
                            .attr("y1", (d) => d.source.y)
                            .attr("x2", (d) => d.target.x)
                            .attr("y2", (d) => d.target.y);

                    node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
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

                    return d3
                            .drag()
                            .on("start", dragstarted)
                            .on("drag", dragged)
                            .on("end", dragended);
                }
            });
</script>
```

- **Explanation:**
    - This D3.js visualization uses a force-directed graph to display the family tree. Nodes represent family members,
      and links represent relationships such as parent-child or siblings. The tree can be dynamically updated based on
      user input, showing different parts of the family hierarchy.

---

#### **Dynamic Interaction and Exploration**

- **User Input:**

Enhance the application by allowing users to enter a person’s name, which then triggers a request to the backend to
fetch and display that person’s family tree.

```html
<input type="text" id="person-name" placeholder="Enter a name"/>
<button onclick="loadFamilyTree()">Load Family Tree</button>

<script>
    function loadFamilyTree() {
        const name = document.getElementById("person-name").value;
        fetch(`/family-tree/${name}`)
                .then((response) => response.json())
                .then((data) => {
                    // Update the D3 visualization with the retrieved data
                });
    }
</script>
```

- **Explanation:**
    - This allows users to explore the family tree interactively. They can enter different names to view the
      corresponding family trees, which the D3.js visualization updates dynamically.

---

#### **Deploying the Application**

- **Containerization with Docker:**

Containerize the FastHTML application to ensure it runs consistently across environments.

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- **Deployment to AWS:**
    - Deploy the application to AWS, using Elastic Beanstalk or ECS to manage and scale the service as needed. Ensure
      the application is accessible and performs well, even as the size of the family tree data grows.

---

### **Final Thoughts**

- **Interactive Family Tree Visualization:**
    - This demo illustrates how graph databases can be used to model and visualize complex hierarchical relationships,
      like those in a family tree. The integration of FastHTML, Neo4j, and D3.js provides a powerful and flexible way to
      explore these relationships interactively.

- **Potential Enhancements:**
    - Consider adding features such as saving and loading specific family trees, expanding nodes to reveal hidden family
      members, or even incorporating historical data and timelines into the visualization.

---

### **Further Discussions**

#### **1. LLMs and Graph Dat

abases**

- **Enhancing Data Extraction:**
    - LLMs can assist in extracting entities and relationships from unstructured text (such as books, articles, or web
      pages) and automatically populating a graph database. This can significantly speed up the process of building
      complex knowledge graphs.

- **Improving Query Generation:**
    - LLMs can understand natural language queries and convert them into Cypher queries, making graph databases more
      accessible to non-technical users. For instance, a user could ask, "Show me all family members related to John
      Doe," and the LLM could generate the appropriate Cypher query.

#### **DevOps with Docker and AWS:**

     - Docker enables the easy deployment of applications in containers, ensuring consistency across environments. AWS provides cloud infrastructure that can scale your graph database application as needed. Discuss the importance of these tools in deploying and maintaining graph database applications in a production environment.

### **Conclusion**

- **Recap:**
    - Summarize the key points covered in the session, emphasizing the versatility and efficiency of graph databases for
      modeling complex relationships. Highlight the ease of querying and managing graph data with Cypher, and how modern
      tooling can further enhance the power of graph databases.
- **Encouragement:**
    - Encourage attendees to explore graph databases in their own projects, experiment with Cypher queries, and consider
      how LLMs and modern web frameworks can be integrated into their workflows to build innovative applications.
