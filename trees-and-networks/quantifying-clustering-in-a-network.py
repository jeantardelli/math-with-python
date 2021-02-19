"""
The clustering coefficient of a node measures the interconnectivity between the
nodes nearby (here, nearby means connected by an edge). In effect, it measures
how close the neighboring nodes are to forming a complete network or clique.


The clustering coefficient of a node measures the proportion of the adjacent
nodes that are connected by an edge; that is, two adjacent nodes form a
triangle with the given node. We count the number of triangles and divide
this by the total number of possible triangles that could be formed, given
the degree of the node. Numerically, the clustering coefficient at a node,
u, in a simple unweighted network is given by the following equation:

    c_u = (2 * T_u) / (deg(u) * deg(u) - 1)

Where T_u is the number of triangles at u and the denominator is the total
possible number of triangles at u.
"""
import networkx as nx
import matplotlib.pyplot as plt

complete_part = nx.complete_graph(4)
cycle_part = nx.cycle_graph(range(4, 9))

G = nx.Graph()
G.update(complete_part)
G.update(cycle_part)
G.add_edges_from([(0, 8), (3, 4)])

fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)
ax.set_title("Network with different clustering behaviour")

cluster_coeffs = nx.clustering(G)

for i in [0, 2, 6]:
    print(f"Node {i}, clustering {cluster_coeffs[i]}")
    # Node 0, clustering 0.5
    # Node 2, clustering 1.0
    # Node 6, clustering 0

av_clustering = nx.average_clustering(G)
print(av_clustering)
# 0.3333333333333333

plt.show()
