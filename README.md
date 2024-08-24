# Fundamentals of working with Graph Databases
## Introduction  

![What is a graph database? The role of graphs in data analysis](https://www.lytics.com/wp-content/uploads/2022/04/article-What-is-a-graph-database.jpg)
### **What is a Graph Database?**  
A graph database is a type of NoSQL database that models data in a graph format, using nodes, edges (relationships), and  
properties. Unlike traditional relational databases that use tables, graph databases are designed to highlight the  
relationships between data points, making them ideal for complex queries and analyses where connections between entities  
are important.  
  
### **Why choose a Graph Database?**  
Graph databases like Neo4J are particularly useful when the relationships between data points are as important as the data itself. Here are some reasons why someone might choose a graph database over a Relational Database Management System (RDBMS) or Document Database:  
  
1. **Relationship Handling**: In graph databases, relationships are first-class citizens and are stored at the individual record level, not computed at query time. This makes traversing relationships much faster compared to RDBMS where joins are computationally expensive.  
2. **Flexibility**: Graph databases are schema-less, which means you can add new types of relationships, nodes, or properties to your graph without disturbing existing application functionality. This is harder to achieve in RDBMS due to its rigid schema.  
3. **Performance**: Graph databases can execute deep, complex queries faster than RDBMS or Document Databases. This is because they can traverse millions of connections per second per core.  
4. **Real-time Insights**: Graph databases like Neo4J can provide real-time insights by executing complex queries on connected data in real time.  
  
For example, consider a social networking application. In an RDBMS, finding all friends-of-friends-of-friends would require a three-table join, which could be slow on a large dataset. In a graph database, this operation is fast because the relationships between users are stored as direct connections.  
  
Similarly, in a recommendation engine, a graph database could quickly suggest products based on a user's behavior and the behavior of other users in the same network. In an RDBMS, this operation could involve complex queries and multiple table joins, which could be slow and inefficient.  
  ![Northwind RDBMS model](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/2-property-graphs/3-rdbms-to-graph/images/northwind.jpg)

[Northwind Example](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/2-property-graphs/3-rdbms-to-graph/)  

[Index Free Adjacency](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/2-property-graphs/2-native-graph/)

### Use Cases:  
**Recommendation Engines:**  
Companies like Amazon and Netflix use graph databases to analyze user behavior and recommend products or content based  
on patterns of similarity and shared interests among users.  
  
**Fraud Detection:**  
Financial institutions use graph databases to detect fraudulent activity by analyzing transactions and identifying  
suspicious patterns that may indicate money laundering or other illegal activities.  
  
**Knowledge Graphs:**  
Google’s Knowledge Graph organizes information from the web into a comprehensive, connected understanding of facts and  
concepts, improving search results and information retrieval.  
  
### **Examples:**  
  
- 🎬 [Neo4j Movie Graph](https://neo4j.com/graph-examples/)  
- 🕵️‍♂️ [Explore the Panama Papers Graph](https://panamapapers.icij.org/graphs/)  
- 📚 [Wikidata Query Service](https://query.wikidata.org/)  
- 🌐 [YAGO Knowledge Graph](https://yago-knowledge.org/)  
- 📖 [DBpedia SPARQL Endpoint](https://dbpedia.org/sparql)  
  
#### **Graph Elements**

![Moving Toward Smarter Data: Graph Databases and Machine Learning - DZone](https://dz2cdn1.dzone.com/storage/temp/13817670-figure-1.png)

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
Each node or relationship can store properties. For example, an `Author` node could have properties  like `name`, `birthdate`, and `nationality`. These properties provide detailed information that can be used in queries to filter results or retrieve specific data.  
  
#### **Directed and Undirected Graphs**  

![Roads between cities](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/1-graph-thinking/3-graph-structure/images/roads.jpg)

**Node Traversal:**  
In a directed graph, edges have a direction, indicating a one-way relationship between nodes. Traversal in a graph involves moving from one node to another along these directed edges. For example, in the "Books and Authors" graph, you  can traverse from an `Author` to the `Books` they wrote by following the `WROTE` relationship.  

In contrast, an undirected graph does not have a direction associated with its edges. Traversal in an undirected graph  allows movement between nodes in both directions. For example, in the "Books and Authors" graph, you can traverse from  an `Author` to the `Books` they wrote and vice versa, as the relationship is not one-way.  
  ![Michael and Sarah have different strengths of their love](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/1-graph-thinking/3-graph-structure/images/michael-sarah-directed.jpg)

**Characteristics:**  
Directed graphs are used when the relationship between nodes has a clear direction, such as parent-child relationships, dependencies, or sequences. This is crucial in understanding hierarchies or flow processes.  
  
Undirected graphs, on the other hand, are used when the relationship between nodes is bidirectional or does not have a  specific direction. This is useful for modeling relationships where the direction is not important, such as friendships  or collaborations between authors.  
#### **Weighted and Unweighted Graphs**  
  
**Edge Weights:**  
In a weighted graph, edges have a numerical value associated with them, known as the weight. This weight represents the  strength, distance, or cost of the relationship between nodes. For example, in the "Books and Authors" graph, you can  
assign a weight to the `WROTE` relationship to indicate the significance or popularity of a book.  
  
In contrast, an unweighted graph does not assign any numerical value to its edges. The relationships between nodes are  considered to have equal importance or cost. For example, in the "Books and Authors" graph, you can represent  the `WROTE` relationship as unweighted if the importance or popularity of books is not a factor in your analysis.  
  
**Characteristics:**  
Weighted graphs are used when the strength or importance of the relationship between nodes needs to be considered. This is useful for various applications, such as finding the shortest path between nodes based on the least weighted edges or  determining the most influential nodes in a network.  
  
Unweighted graphs, on the other hand, are used when the relationships between nodes are considered to have equal  importance or when the focus is on the structure of the graph rather than the specific weights of the edges.  
  
#### **Performance Advantage over RDBMS**  
  
In a relational database, retrieving connected data often requires expensive join operations between tables, which can  become slow as data grows. In a graph database, each node directly references its adjacent nodes through relationships,  allowing for fast and efficient traversals without needing to perform joins. This is known as index-free adjacency and  is one of the key advantages of graph databases, especially for queries that require traversing multiple levels of  
connections.  
  
### Getting Started with Neo4j  
  ![Neo4j - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/e/e5/Neo4j-logo_color.png)


- **Graph Database**: Neo4j is a graph database, a type of NoSQL database that uses graph structures to represent and store data.

- **Relationships**: It emphasizes relationships between data points, making it ideal for handling complex, interconnected data.

- **Schema-less**: Neo4j is schema-less, allowing for flexibility in data modeling and evolution over time.

- **Cypher Query Language**: It uses a declarative, SQL-inspired language called Cypher for querying and manipulating the graph.

- **Performance**: Neo4j is designed for high performance, capable of traversing millions of relationships per second per core.

- **Real-time Insights**: It can provide real-time insights by executing complex queries on connected data in real time.

- **Use Cases**: It's widely used in various industries for use cases such as recommendation engines, fraud detection, real-time graph analytics, network and IT operations, identity and access management, and more.


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
2. Create docker-compose.yaml file:  
  
```yaml  
services:
	graphdb:  
	  image: neo4j:5.22.0  
	  ports:  
	    - "7474:7474"  
	    - "7687:7687"  
	  environment:  
	    - NEO4J_AUTH=neo4j/password  
	  volumes:  
	    - ./n4jdb/data:/data  
	    - ./n4jdb/import:/import  
	    - ./n4jdb/logs:/logs 
```  
  
3. Bring up the service:  
  
```bash  
docker compose -f docker-compose.yaml up
```  
  
4. You can then access the Neo4j Browser at `http://localhost:7474` and connect to your database using the credentials  
   you provided.  
  
#### Introduction to Cypher  
  
**Cypher Query Language:**  
Cypher is a powerful, expressive query language designed specifically for querying and manipulating graph databases. It allows you to describe patterns in your data graphically, making it intuitive to write queries.  
  
##### Basic Structure of Cypher Query  
  
A Cypher query consists of several components:  
  
1. **MATCH:** This keyword is used to specify the pattern of nodes and relationships to match in the graph.  
  
2. **Nodes and Relationships:** Nodes are represented by parentheses, and relationships are represented by hyphens. The  direction of the relationship can be specified using arrows (-> for outgoing, <- for incoming, and -- for  bidirectional).  
  
3. **Labels and Properties:** Labels are used to categorize nodes, and properties are key-value pairs that provide additional information about nodes and relationships.  
  
4. **RETURN:** This keyword is used to specify the data to be returned as the result of the query.  
  
Here's an example of a basic Cypher query structure:  
  
```cypher  
MATCH (a:Label1)-[:RELATIONSHIP]->(b:Label2)  
RETURN a.property1, b.property2  
```  
  
In this example, the query matches nodes labeled as "Label1" connected to nodes labeled as "Label2" via a "RELATIONSHIP" relationship. The query then returns the values of "property1" from node "a" and "property2" from node "b".  
  
Remember to replace "Label1", "Label2", "RELATIONSHIP", "property1", and "property2" with the actual labels and properties relevant to your graph database.  
  
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
  
In this example, replace Label with the label for the nodes you're creating, property1 and property2 with the property  names, and column1 and column2 with the column names from your CSV file. Please note that the file path in the LOAD CSV  command is relative to the Neo4j import directory. If you're running Neo4j Desktop, this is typically the import  
directory inside your Neo4j database folder.  
  
##### **Loading Author and Book Data**  
  
Files for the Author and Book demo can be found in the `data` directory of the project.  
  
```cypher  
LOAD CSV WITH HEADERS FROM 'file:///books/series.csv' AS row  
CREATE (:Series {series_id: row.series_id, name: row.name});  
  
LOAD CSV WITH HEADERS FROM 'file:///books/authors.csv' AS row  
CREATE (:Author {author_id: row.author_id, name: row.name, birthdate: row.birthdate, nationality: row.nationality});  
  
  
LOAD CSV WITH HEADERS FROM 'file:///books/books.csv' AS row  
CREATE (:Book {book_id: row.book_id, title: row.title, publication_year: toInteger(row.publication_year), ISBN: row.ISBN, genre: row.genre});  
  
LOAD CSV WITH HEADERS FROM 'file:///books/wrote_relationship.csv' AS row  
MATCH (a:Author {author_id: row.author_id}), (b:Book {book_id: row.book_id})  
CREATE (a)-[:WROTE {role: row.role, contribution_percentage: toFloat(row.contribution_percentage)}]->(b);  
  
LOAD CSV WITH HEADERS FROM 'file:///books/belongs_to_series.csv' AS row  
MATCH (b:Book {book_id: row.book_id}), (s:Series {series_id: row.series_id})  
CREATE (b)-[:BELONGS_TO {book_number: toInteger(row.book_number)}]->(s);  
```  
  
#### **Loading Person and Relationship Data**  
  
```cypher  
// Create uniqueness constraints  
CREATE CONSTRAINT FOR (p:Person) REQUIRE p.person_id IS UNIQUE;  
  
// Load persons data  
LOAD CSV WITH HEADERS FROM 'file:///person.csv' AS row  
CREATE (:Person {person_id: toInteger(row.person_id), name: row.name, birthdate: date(row.birthdate), gender: row.gender, birthplace: row.birthplace});  
  
// Load parent-child relationships  
LOAD CSV WITH HEADERS FROM 'file:///relationships.csv' AS row  
MATCH (parent:Person {person_id: toInteger(row.parent_id)}), (child:Person {person_id: toInteger(row.child_id)})  
CREATE (parent)-[:PARENT_OF]->(child);  
```  
  
### **Building a Web Application with Python Tooling and D3.js**  
  
In this demo, we will provide more detailed setup instructions and implementation guidance for building a web  application that visualizes the relationships between authors and books using Python, FastAPI, Neo4j, FastHTML, and  D3.js. The project will be structured for easy development, using Rye for Python package management and FastHTML for  
templating.  
  
### Python    

![Step-by-Step Guide to Building a REST API with Flask and SQLAlchemy for  Tracking PTO Requests](https://static.wixstatic.com/media/c518ae_939737ad329740dfa069cdab6461e416~mv2.jpg/v1/fill/w_1000,h_500,al_c,q_85,usm_0.66_1.00_0.01/c518ae_939737ad329740dfa069cdab6461e416~mv2.jpg)

Python is a high-level, interpreted programming language with dynamic semantics. It's built-in data structures, combined    
with dynamic typing and dynamic binding, make it an ideal language for scripting and rapid application development.    
Python supports modules and packages, encouraging program modularity and code reuse.    
    
Python is particularly well-suited for data visualization for several reasons:    
     
1. **Accessible Syntax**: Python's clear and intuitive syntax makes it easy to learn, read, and write. This    
   accessibility    
   extends to its data visualization libraries, which are designed to be user-friendly and straightforward.    
    
2. **Extensive Libraries**: Python has a rich ecosystem of libraries, including several powerful options for data  visualization like Matplotlib, Seaborn, Plotly, and Bokeh. These libraries offer a wide range of features and  customization options, allowing you to create high-quality, interactive visualizations.    
    
3. **Community Support**: Python has a large and active community, which means you can find a wealth of resources,  tutorials, and code snippets to help you with your data visualization tasks. If you encounter a problem or need help, chances are someone else has already faced the same issue and you can find help and solutions online.    
    
4. **Data Science Support**: Python is a popular language in the data science community. Libraries like NumPy, Pandas,  and  SciPy provide robust support for tasks like data cleaning, analysis, and transformation, which are often necessary    
   steps before data can be visualized.    
  
### HTMX 

![htmx: how frontend can be made easy and fun | by Jose Granja | Medium](https://miro.medium.com/v2/resize:fit:1000/0*eAwgKaeGdkhVqWcg.png)

HTMX is a modern HTML-first AJAX library that allows you to access AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML, using attributes, so you can build modern user interfaces with the simplicity and power of hypertext.  
  
Here's a basic example of how you can use HTMX to create a simple web page:  
  
```html  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>HTMX Example</title>  
    <script src="https://unpkg.com/htmx.org@1.6.1"></script>  
</head>  
<body>  
    <div id="content" hx-get="/updateContent" hx-trigger="every 5s">  
        Initial content  
    </div>  
</body>  
</html>  
```  
  
In this example, the `hx-get` attribute tells HTMX to issue a GET request to the `/updateContent` URL. The `hx-trigger` attribute tells HTMX to issue this request every 5 seconds. The response from the server will replace the innerHTML of the `div`.  
  
On the server side, you would have an endpoint `/updateContent` that returns the new content for the `div`. Here's a simple example using FastAPI:  
  
```python  
from fastapi import FastAPI  
  
app = FastAPI()  
  
@app.get("/updateContent")  
async def update_content():  
    # Replace with your actual logic to generate new content  
    return "Updated content"  
```  
  
  
In this example, the `/updateContent` endpoint returns a string "Updated content". This string will replace the innerHTML of the `div` every 5 seconds.  
  
Please note that you need to run the FastAPI application and replace `/updateContent` with the actual URL of the running application (e.g., `http://localhost:8000/updateContent`).  
  
### FastHTML  

![GitHub - AnswerDotAI/fasthtml: The fastest way to create an HTML app](https://repository-images.githubusercontent.com/801880448/6808117b-5b6a-4a57-92d2-aa6d29ec2ce8)

FastHTML is a Python library that provides a simple and intuitive way to generate HTML content. It's built on top of the FastAPI framework, making it an excellent choice for building web applications with Python. Here are several reasons why FastHTML is well-suited for web development:  
  
1. **Simplicity**: FastHTML uses Python's syntax to generate HTML content, making it easy to learn and use. You can create HTML elements as Python objects and nest them to build complex structures.  
  
2. **Integration with FastAPI**: FastHTML is designed to work seamlessly with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. This integration allows you to leverage FastAPI's features like dependency injection, routing, and validation in your web application.  
  
3. **Dynamic Content Generation**: With FastHTML, you can generate dynamic HTML content based on your application's data. This is done by passing data to your HTML elements and using Python's logic to manipulate and display the data.  
  
4. **Component-Based Structure**: FastHTML promotes a component-based structure, where you can create reusable HTML components and use them across your application. This can lead to cleaner and more maintainable code.  
  
Here's a basic example of how you can use FastHTML to create a simple web page:  
  
```python  
from fasthtml import Div, H1, P  
from fasthtml.fastapp import fast_app, serve  
  
app, route = fast_app()  
  
@route('/')  
def get():  
    return Div(  
        H1("Welcome to FastHTML!"),  
        P("FastHTML is a Python library for generating HTML content.")  
    )  
  
if __name__ == "__main__":  
    serve()  
  
```  
  
In this example, `Div`, `H1`, and `P` are HTML elements represented as Python objects. The `fast_app` function creates a FastAPI application, and the `route` decorator defines a route for the application. The `get` function returns a `Div` element containing an `H1` and a `P` element, which will be rendered as HTML when the route is accessed. The `serve` function starts the application.  
  
### D3.js  

![Interactive Data Visualization with D3.js | by Dipanjan (DJ) Sarkar |  Towards Data Science](https://miro.medium.com/v2/resize:fit:2694/1*1HC_tkU_Kt-VjAgCd7fdRA.png)

D3.js (or just D3 for Data-Driven Documents) is a JavaScript library that allows you to bind arbitrary data to a Document Object Model (DOM), and then apply data-driven transformations to the document. It is a powerful tool for creating and manipulating complex visualizations on the web.  
  
Here are several reasons why D3.js is well-suited for data visualization:  
  
1. **Flexibility**: D3.js does not restrict you to a specific framework or chart type. You can create anything from a simple bar chart to complex infographics and interactive animations.  
  
2. **Data-Driven**: D3.js allows you to bind data to the DOM and apply transformations to the document based on that data. This makes it easier to generate complex visualizations and apply dynamic behaviors to them.  
  
3. **Integration with Web Standards**: D3.js uses standard web technologies such as SVG, HTML, and CSS. This means you can use it with any modern browser without requiring any additional plugins.  
  
4. **Powerful Tools**: D3.js provides powerful tools for creating scales, color schemes, shapes, layouts, and more. It also supports user interactions, animations, and transitions.  
  
Here's a basic example of how you can use D3.js to create a simple bar chart:  
  
```javascript  
// Sample data  
const data = [4, 8, 15, 16, 23, 42];  
  
// Create a scaling function  
const scale = d3.scaleLinear()  
    .domain([0, d3.max(data)])  
    .range([0, 420]);  
  
// Select the chart container and bind the data to it  
d3.select(".chart")  
  .selectAll("div")  
  .data(data)  
  .enter().append("div")  
    .style("width", d => scale(d) + "px")  
    .text(d => d);  
```  
  
In this example, `d3.scaleLinear()` creates a linear scaling function that maps the domain (input values) to the range (output values). The `d3.select()` function selects the chart container, and the `data()` function binds the data to the document. The `enter().append("div")` part creates a new div for each data point. The `style()` function sets the width of each bar based on the data, and the `text()` function sets the text of each bar to the data value.  
  
Please note that D3.js has a steep learning curve due to its flexibility and low-level nature. However, once you get the hang of it, you can create almost any kind of data visualization you can imagine.  
  
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
│   │   ├── main.py            # FastHTML application setup  
│   │   └── public/  
│   │       └── js/  
│   │           └── graph.js   # D3.js code  
└── .env                       # Environment variables  
```  
  
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

3. Create a `.env` file in the project root to store environment variables:  

   ```  
   NEO4J_URI=bolt://localhost:7687  
   NEO4J_USER=neo4j  
   NEO4J_PASSWORD=password  
   ```  
#### **Connecting to the Neo4j Database**  
  
**`database.py`:**  
  
```python  
 
def get_driver(database: str = None) -> Driver:  
    uri = os.getenv("NEO4J_URI")  
    auth = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))  
    return GraphDatabase.driver(uri=uri, auth=auth, database=database)  
  
  
def get_async_driver(database: str = None) -> AsyncDriver:  
    uri = os.getenv("NEO4J_URI")  
    auth = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))  
    return AsyncGraphDatabase.driver(uri=uri, auth=auth, database=database)  
  
  
def create_database(driver: Driver, name: str):  
    result = driver.execute_query(  
        f"CREATE DATABASE {name}", routing_=RoutingControl.WRITE  
    )  
    return result  
  
  
def query_one(driver: Driver, query: str) -> Record:  
    record = driver.execute_query(query, record_transformer_=Result.single)  
    return record  
  
  
def query_many(driver: Driver, query: str) -> List[Record]:  
    records = driver.execute_query(query, result_transformer_=EagerResult.records)  
    return records  
  
  
async def async_query_one(driver: AsyncDriver, query: str) -> Record:  
    record = await driver.execute_query(query, record_transformer_=AsyncResult.single)  
    return record  
  
  
async def async_query_many(driver: AsyncDriver, query: str) -> EagerResult:  
    results = await driver.execute_query(query)  
    return results  
  
```  
  
**`main.py`:**  
  
```python  
STANDALONE_KEY = "Standalone"  
CHILDREN_KEY = "children"  
NAME_KEY = "name"  
GRAPH_DATA_QUERY = """  
    MATCH (a:Author)-[:WROTE]->(b:Book)  
    OPTIONAL MATCH (b)-[:BELONGS_TO]->(s:Series)  
    RETURN a.name AS author, b.title AS book, s.name AS series  
    """  
  
DATABASE = "books"  
  
app, route = fast_app(  
    debug=True,  
    live=True,  
)  
  
  
@route("/{fname:path}.{ext:static}")  
async def get(fname: str, ext: str):  
    return FileResponse(f"public/{fname}.{ext}")  
  
  
@route("/graph-data")  
async def get(request):  # Query Neo4j database for authors and books  
    async with get_async_driver(database=DATABASE) as driver:  
        data = await async_query_many(driver, GRAPH_DATA_QUERY)  
        root = format_graph_data(data)  
        return JSONResponse(root)  
  
  
def format_graph_data(data: EagerResult):  
    authors = {}  
  
    for record in data.records:  
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
            Nav(  
                A("Graph DB Fundamentals", href="/", cls="link dim white b f6 f5-ns dib mr3"),  
                A("Home", href="/", cls="link dim light-gray f6 f5-ns dib mr3"),  
                cls="pa3 pa4-ns"),  
            H2("Books and Authors Visualization", cls="mt5 tc"),  
            Main(Div(Div(id="graph", cls="mt4"), cls="center")),  
            Script(src="https://d3js.org/d3.v6.min.js"),  
            Script(src="/public/js/graph.js"))  
  
  
if __name__ == "__main__":  
    serve(port=8000, reload=True)  
  
```  
  
#### **Adding D3.js Visualization**  
  
**`public/js/graph.js`:**  
  
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
  .style("color", "black")  // Ensure the text color is black  
  .style("font-size", "12px");  
  
  
  // Draw the arcs (sunburst segments)  
  const paths = svg.append("g")  
    .attr("fill-opacity", 0.6)  
    .selectAll("path")  
    .data(root.descendants().filter(d => d.depth))  
    .join("path")  
    .attr("fill", d => { while (d.depth > 1) d = d.parent; return color(d.data.name); })  
    .attr("d", arc)  
    .on("mouseover", function(event, d) {  
      tooltip.style("visibility", "visible")  
        .text(d.data.name); // Display the full text in the tooltip  
      d3.select(this).attr("fill-opacity", 1); // Darken the opacity on hover  
    })  
    .on("mousemove", function(event) {  
      tooltip.style("top", (event.pageY - 10) + "px")  
        .style("left", (event.pageX + 10) + "px");  
    })  
    .on("mouseout", function(event, d) {  
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
    .attr("transform", function(d) {  
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
  
### Running the Application  
  
1. **Start the server using Uvicorn:**  
  
   ```bash  
   rye run uvicorn app.books:app --reload  
   ```  
   
1. **Access the application in your browser:**  
   - Navigate to `http://localhost:8000/` to view the D3.js visualization of the "Books and Authors" graph.   
  
#### **Deploying the Application**  
  
TODO  
  
### **Building a Web Application to Visualize a Family Tree with Python Tooling and D3.js**  
  
In this demo, we'll walk through the process of creating a web application that visualizes a family tree using a graph database schema. The application will allow users to explore the hierarchical relationships within a family, such as  parent-child and sibling relationships. The backend will be powered by FastAPI, and the frontend will use D3.js to render the family tree.  
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
  
**Example Data:**  
  
Nodes:  
  
- Person: `{name: "John Doe", birthdate: "1980-01-15", gender: "Male", birthplace: "New York"}`  
- Person: `{name: "Jane Doe", birthdate: "1978-03-22", gender: "Female", birthplace: "New York"}`  
- Person: `{name: "Alice Doe", birthdate: "2005-07-18", gender: "Female", birthplace: "New York"}`  
  
Relationships:  
  
- `(John Doe)-[:PARENT_OF]->(Alice Doe)`  
- `(Jane Doe)-[:PARENT_OF]->(Alice Doe)`  
  
#### **Setting Up the Backend with FastHTML**  
  
**`tree.py`:**  
  
```python   
app, rt = fast_app(live=True, debug=True)  
  
GRAPH_DATA_QUERY = """  
MATCH (p:Person)-[:PARENT_OF]->(descendant:Person)  
RETURN p, descendant;  
"""  
  
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
    async with get_async_driver(database=DATABASE) as driver:  
        data = await async_query_many(driver, GRAPH_DATA_QUERY)  
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
  
```  
  
#### **Building the Frontend with D3.js**  
**`public/js/tree.js`:**  
```js  
document.addEventListener("DOMContentLoaded", async () => {  
    // Fetch the data from the backend  
    const response = await fetch("/tree");  
    const data = await response.json();  
  
    const width = 1200;  
    const height = 800;  
    const margin = {top: 40, right: 120, bottom: 20, left: 120};  
    const cardWidth = 150;  
    const cardHeight = 50;  
    // Define the background color here  
    const backgroundColor = "#1c1c1c";  // Use the color from the uploaded image  
  
    const svg = d3  
        .select("#family-tree")  
        .append("svg")  
        .attr("width", width + margin.right + margin.left)  
        .attr("height", height + margin.top + margin.bottom)  
        .style("background-color", backgroundColor)  // Set the background color  
        .style("border", "1px solid white")  // Add a white border  
        .call(d3.zoom().on("zoom", function (event) {  
            svg.attr("transform", event.transform);  
        }))  
        .append("g")  
        .attr("transform", `translate(${margin.left},${margin.top})`);  
  
    const root = d3.hierarchy(data);  
    root.x0 = height / 2;  
    root.y0 = 0;  
  
    // Tree layout with increased separation between columns  
    const treeLayout = d3.tree()  
        .size([height, width - margin.left - margin.right])  
        .separation((a, b) => (a.parent === b.parent ? 2 : 3)); // Increase separation between sibling nodes  
  
    const update = (source) => {  
        // Assign the new positions for the nodes  
        treeLayout(root);  
  
        const nodes = root.descendants();  
        const links = root.descendants().slice(1);  
  
        // Adjust y position to increase space between columns  
        nodes.forEach(d => {  
            d.y = d.depth * 250;  // Increase horizontal spacing by adjusting depth multiplier  
            d.x *= 1.5;  // Increase vertical spacing by scaling the x position  
        });  
  
        // Update the nodes  
        const node = svg.selectAll("g.node")  
            .data(nodes, d => d.id || (d.id = ++i));  
  
        const nodeEnter = node.enter().append("g")  
            .attr("class", "node")  
            .attr("transform", d => `translate(${source.y0},${source.x0})`)  
            .on("click", click);  
  
        nodeEnter.append("rect")  
            .attr("width", cardWidth)  
            .attr("height", cardHeight)  
            .attr("x", -cardWidth / 2)  
            .attr("y", -cardHeight / 2)  
            .attr("fill", d => d._children ? "#9b3df4" : "#e1bcff")  
            .attr("stroke", "#e1bcff")  
            .attr("stroke-width", "2px")  
            .attr("rx", 10)  
            .attr("ry", 10);  
  
        nodeEnter.append("text")  
            .attr("dy", ".35em")  
            .attr("x", 0)  
            .attr("text-anchor", "middle")  
            .attr("fill", "#000")  
            .text(d => d.data.name);  
  
        const nodeUpdate = nodeEnter.merge(node);  
  
        nodeUpdate.transition()  
            .duration(750)  
            .attr("transform", d => `translate(${d.y},${d.x})`);  
  
        nodeUpdate.select("rect")  
            .attr("fill", d => d._children ? "#9b3df4" : "#e1bcff");  
  
        nodeUpdate.select("text")  
            .style("fill-opacity", 1);  
  
        const nodeExit = node.exit().transition()  
            .duration(750)  
            .attr("transform", d => `translate(${source.y},${source.x})`)  
            .remove();  
  
        nodeExit.select("rect")  
            .attr("width", 1e-6)  
            .attr("height", 1e-6);  
  
        nodeExit.select("text")  
            .style("fill-opacity", 1e-6);  
  
        // Update the links  
        const link = svg.selectAll("path.link")  
            .data(links, d => d.id);  
  
        const linkEnter = link.enter().insert("path", "g")  
            .attr("class", "link")  
            .attr("d", d => {  
                const o = {x: source.x0, y: source.y0};  
                return diagonal({source: o, target: o});  
            })  
            .attr("fill", "none")  
            .attr("stroke", "#ccc")  
            .attr("stroke-width", "2px");  
  
        const linkUpdate = linkEnter.merge(link);  
  
        linkUpdate.transition()  
            .duration(750)  
            .attr("d", d => diagonal({source: d.parent, target: d}));  
  
        const linkExit = link.exit().transition()  
            .duration(750)  
            .attr("d", d => {  
                const o = {x: source.x, y: source.y};  
                return diagonal({source: o, target: o});  
            })  
            .remove();  
  
        nodes.forEach(d => {  
            d.x0 = d.x;  
            d.y0 = d.y;  
        });  
    };  
  
    const click = (event, d) => {  
        if (d.children) {  
            d._children = d.children;  
            d.children = null;  
        } else {  
            d.children = d._children;  
            d._children = null;  
        }  
        update(d);  
    };  
  
    const collapse = (d) => {  
        if (d.children) {  
            d._children = d.children;  
            d._children.forEach(collapse);  
            d.children = null;  
        }  
    };  
  
    const expandAll = () => {  
        root.each(d => {  
            if (d._children) {  
                d.children = d._children;  
                d._children = null;  
            }  
        });  
        update(root);  
        document.querySelector("#expand-all").style.display = "none";  
        document.querySelector("#collapse-all").style.display = "block";  
    };  
  
    const collapseAll = () => {  
        root.each(collapse);  
        update(root);  
        document.querySelector("#expand-all").style.display = "block";  
        document.querySelector("#collapse-all").style.display = "none";  
    }  
  
    d3.select("#expand-all").on("click", expandAll);  
    d3.select("#collapse-all").on("click", collapseAll);  
  
    const diagonal = d3.linkHorizontal()  
        .x(d => d.y)  
        .y(d => d.x);  
  
    let i = 0;  
    root.children.forEach(collapse); // Start with all nodes collapsed  
    update(root);  
});  
  
document.querySelector('.info-icon').addEventListener('mouseenter', () => {  
    const banner = document.querySelector('.info-banner');  
    banner.style.display = banner.style.display === 'block' ? 'none' : 'block';  
});  
  
document.querySelector('.close-btn').addEventListener('click', () => {  
    document.querySelector('.info-banner').style.display = 'none';  
});  
```  
  
#### **Deploying the Application**  
TODO  
  
#### **Containerization with Docker:**  
TODO