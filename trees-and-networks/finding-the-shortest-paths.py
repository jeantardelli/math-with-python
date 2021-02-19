"""
A common problem where networks make an appearance is in the problem of finding
the shortest – or perhaps more precisely, the highest reward – route between
two nodes in a network. For instance, this could be the shortest distance
between two cities, where the nodes represent the cities and the edges are
roads connecting pairs of cities. In this case, the weights of the edges would
be their lengths.

This module illustrates how to find the shortest path bewteen two nodes.
"""
import networkx as nx
import matplotlib.pyplot as plt

from numpy.random import default_rng

rng = default_rng(12345)
G = nx.gnm_random_graph(10, 17, seed=12345)

fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)
ax.set_title("Random network for shortest path finding")

for u, v in G.edges:
    G.edges[u, v]["weight"] = rng.integers(5, 15)

path = nx.shortest_path(G, 7, 9, weight="weight")
print(path)
# [7, 5, 2, 9]

length = nx.shortest_path_length(G, 7, 9, weight="weight")
print(f"Lenght: {length}")
# Length 32

plt.show()
