# PRACTICAL 6 - Louvain algorithm using Neo4j Graph Data Science (GDS)
# Install: pip install neo4j graphdatascience pandas
# Before running: Neo4j instance must be STARTED and GDS plugin installed.
# Change PASSWORD below to the password you set for your Neo4j instance.

from graphdatascience import GraphDataScience

# Step 1: Connect to Neo4j
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "your_password"

gds = GraphDataScience(URI, auth=(USERNAME, PASSWORD))
print("Connected to Neo4j successfully!")
print("GDS version:", gds.version())


# Step 2: Clear old data and create sample nodes and relationships
gds.run_cypher("MATCH (n) DETACH DELETE n")

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


# Step 3: Project the graph into GDS memory
if gds.graph.exists("socialGraph")["exists"]:
    gds.graph.get("socialGraph").drop()

G, _ = gds.graph.project(
    "socialGraph",
    "Person",
    {"FRIEND": {"orientation": "UNDIRECTED"}}
)
print("Graph projection completed!")


# Step 4: Run Louvain
result = gds.louvain.stream(G)

names = gds.run_cypher("MATCH (p:Person) RETURN id(p) AS nodeId, p.name AS Person")

output = (
    result.merge(names, on="nodeId")[["Person", "communityId"]]
    .sort_values(["communityId", "Person"])
    .reset_index(drop=True)
)

print("\nLouvain Community Detection Results:")
print(output)


# Step 5: Cleanup
G.drop()
gds.close()
print("\nLouvain algorithm executed successfully!")
