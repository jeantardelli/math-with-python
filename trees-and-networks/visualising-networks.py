"""
A common first step in analyzing a network is to draw the network, which can
help us identify some of the prominent features of a network. This module
illustrates how to visualize a network in Python.
"""
import networkx as nx
import matplotlib.pyplot as plt

# Graph from "Creating networks" recipe
G = nx.Graph()

G.add_nodes_from(range(1, 7))
G.add_edges_from([
    (1, 2), (2, 3), (3, 4), (3, 5),
    (3, 6), (4, 5), (5, 6)])

fig, ax = plt.subplots()

layout = nx.shell_layout(G)

nx.draw(G, ax=ax, pos=layout, with_labels=True)
ax.set_title("Simple network drawing")

plt.show()
