# Advantages of Neo4j Over SQL: A Business Perspective

## 1. Business Question

Find all customers who have ordered a specific product.

In SQL, you would need to join the `Customers`, `Orders`, `Order Details`, and `Products` tables. In Neo4j, you can
simply traverse the graph from the `Product` node to the `Customer` nodes through the `ORDERED` relationship.

### In SQL:

```SQL
SELECT c.CustomerID, c.CompanyName
FROM Customers c
         JOIN Orders o ON c.CustomerID = o.CustomerID
         JOIN OrderDetails od ON o.OrderID = od.OrderID
         JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductID = 1;
```

### Schema in Neo4j:

```cypher
CREATE (c:Customer {customerID: "ALFKI", companyName: "Alfreds Futterkiste"})
CREATE (p:Product {productID: 1, productName: "Chai"})
CREATE (o:Order {orderID: 10248})
CREATE (c)-[:PLACED]->(o)
CREATE (o)-[:CONTAINS]->(p)
```

### Cypher query for all customers who have ordered a specific product:

```cypher
MATCH (c:Customer)-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product {productName: "Chai"})
RETURN c.companyName
```

## 2. **Business Question:**

"Find all the products that have been purchased by customers who live in the same city."

### In SQL:

To accomplish this in SQL, you would need to write a query that joins the `Customers`, `Orders`, and `OrderDetails`
tables, and then possibly join it again with the `Products` table. The query would also need to filter customers who
live in the same city, making the SQL query somewhat complex:

```sql
SELECT DISTINCT p.ProductName
FROM Customers c1
         JOIN Orders o1 ON c1.CustomerID = o1.CustomerID
         JOIN OrderDetails od1 ON o1.OrderID = od1.OrderID
         JOIN Products p ON od1.ProductID = p.ProductID
WHERE EXISTS (SELECT 1
              FROM Customers c2
                       JOIN Orders o2 ON c2.CustomerID = o2.CustomerID
                       JOIN OrderDetails od2 ON o2.OrderID = od2.OrderID
              WHERE c2.City = c1.City
                AND od2.ProductID = p.ProductID);
```

### In Neo4j (Cypher Query):

```cypher
MATCH (c1:Customer)-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product)<-[:CONTAINS]-(:Order)<-[:PLACED]-(c2:Customer)
WHERE c1.city = c2.city
RETURN DISTINCT p.name;
```


## 3. Business Question

"Find all customers who have ordered more than 5 different products."

### In SQL:
In SQL, you would need to join the Customers, Orders, Order Details, and Products tables, and then group by CustomerID and filter by the count of distinct ProductID
```SQL
SELECT c.CustomerID, c.CompanyName
FROM Customers c
         JOIN Orders o ON c.CustomerID = o.CustomerID
         JOIN OrderDetails od ON o.OrderID = od.OrderID
GROUP BY c.CustomerID, c.CompanyName
HAVING COUNT(DISTINCT od.ProductID) > 5;
```

### In Neo4j (Cypher Query):
In Neo4j, you can traverse the graph from the Customer nodes to the Product nodes through the ORDERED relationship, and then filter by the count of distinct Product nodes:
```cypher
MATCH (c:Customer)-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product)
WITH c, COUNT(DISTINCT p) AS productCount
WHERE productCount > 5
RETURN c.customerID, c.companyName;
```


# Why It's Easier in Neo4j:

- **Direct Relationships:** In Neo4j, you can directly express the relationships between entities (like customers,
  orders, and products) without needing to worry about complex joins.
- **Simplified Query:** The query clearly expresses the pattern you're looking for (customers who bought the same
  product and live in the same city) using a simple MATCH clause.
- **Natural Representation:** The graph structure naturally represents relationships, making it easier to query patterns
  like this.
