import logging
from graphdatascience import GraphDataScience

# Hide Neo4j deprecation warnings (the red text)
logging.getLogger("neo4j").setLevel(logging.ERROR)
logging.getLogger("neo4j.notifications").setLevel(logging.ERROR)

# Step 1: Connect to Neo4j
URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"

gds = GraphDataScience(URI, auth=(USERNAME, PASSWORD))
print("Connected to Neo4j successfully!")

# Step 2: Clear old data and any old projection
gds.run_cypher("MATCH (n) DETACH DELETE n")
gds.run_cypher("CALL gds.graph.drop('friends', false)")

# Step 3: Create nodes and relationships
gds.run_cypher("""
CREATE
(a:Person {name: 'Amit'}),
(b:Person {name: 'Rahul'}),
(c:Person {name: 'Priya'}),
(d:Person {name: 'Simran'}),
(e:Person {name: 'Karan'}),
(f:Person {name: 'Neha'}),
(a)-[:FRIEND]->(b),
(a)-[:FRIEND]->(c),
(b)-[:FRIEND]->(c),
(d)-[:FRIEND]->(e),
(d)-[:FRIEND]->(f),
(e)-[:FRIEND]->(f),
(c)-[:FRIEND]->(d)
""")
print("Nodes and relationships created!")

# Step 4: Project the graph (UNDIRECTED is required for Louvain)
gds.run_cypher("""
CALL gds.graph.project(
  'friends',
  'Person',
  {FRIEND: {orientation: 'UNDIRECTED'}}
)
""")
print("Graph projection completed!")

# Step 5: Apply Louvain
result = gds.run_cypher("""
CALL gds.louvain.stream('friends')
YIELD nodeId, communityId
RETURN gds.util.asNode(nodeId).name AS Person,
       communityId AS Community
ORDER BY Community, Person
""")

print("\nLouvain Community Detection Results:")
print("Detected Communities:")
print(result)

# Step 6: Clean up
gds.run_cypher("CALL gds.graph.drop('friends')")
gds.close()
print("\nLouvain algorithm executed successfully!")
