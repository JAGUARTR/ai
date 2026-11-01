# PRACTICAL 9 - PageRank using random walk simulation
# Install if required: pip install numpy networkx

import numpy as np
import random

# Directed graph as adjacency matrix (1 = link exists)
graph = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
])

n = len(graph)
steps = 5000
visits = np.zeros(n)

# Start from Page 1
current = 0

for i in range(steps):
    visits[current] += 1
    links = np.where(graph[current] == 1)[0]

    if len(links) > 0:
        current = random.choice(links)
    else:
        current = random.randint(0, n - 1)

pagerank = visits / steps

print("PageRank Results")
print("----------------")
for i in range(n):
    print("Page", i + 1, ":", round(pagerank[i], 4))

print("\nMost Important Page:", np.argmax(pagerank) + 1)


# Sorted nodes as per random walk score
print("\nPages sorted by random walk score:")
for i in np.argsort(-pagerank):
    print("Page", i + 1, ":", round(pagerank[i], 4))


# Compare with inbuilt PageRank (networkx)
import networkx as nx

G = nx.from_numpy_array(graph, create_using=nx.DiGraph)
nx_pr = nx.pagerank(G)

print("\nInbuilt networkx PageRank:")
for node in sorted(nx_pr, key=nx_pr.get, reverse=True):
    print("Page", node + 1, ":", round(nx_pr[node], 4))
