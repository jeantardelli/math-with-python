"""
Networks are objects that contain nodes and edges between pairs of nodes. They
can be used to represent a wide variety of real-world situations, such as
distribution and scheduling. Mathematically, networks are useful for visualizing
combinatorial problems and make for a rich and fascinating theory. This module
shows how to create a simple network in Python.
"""
import networkx as nx

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_nodes_from([3, 4, 5, 6])

G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)])

print(G.nodes)
print(G.edges)
