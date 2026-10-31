# Install first (run in terminal, not inside the script):
# python -m pip install numpy networkx

# PageRank using random walk
import numpy as np
import random

# Directed graph using adjacency matrix
graph = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
])

# Number of pages
n = len(graph)

# Number of random walk steps
steps = 5000

# Store visits to each page
visits = np.zeros(n)

# Start from Page 1
current = 0

# Random walk
for i in range(steps):
    # Count visit
    visits[current] += 1

    # Find connected pages
    links = np.where(graph[current] == 1)[0]

    # If links are available, choose one randomly
    if len(links) > 0:
        current = random.choice(links)
    # If no link is available, choose any page
    else:
        current = random.randint(0, n - 1)

# Calculate PageRank
pagerank = visits / steps

# Display results
print("PageRank Results")
print("----------------")
for i in range(n):
    print("Page", i + 1, ":", round(pagerank[i], 4))

print("\nMost Important Page:", np.argmax(pagerank) + 1)

# Compare with inbuilt PageRank (NetworkX)
import networkx as nx

G = nx.from_numpy_array(graph, create_using=nx.DiGraph)
inbuilt = nx.pagerank(G)

print("\nInbuilt PageRank (NetworkX)")
print("---------------------------")
for node, score in inbuilt.items():
    print("Page", node + 1, ":", round(score, 4))

print("\nMost Important Page (inbuilt):", max(inbuilt, key=inbuilt.get) + 1)
