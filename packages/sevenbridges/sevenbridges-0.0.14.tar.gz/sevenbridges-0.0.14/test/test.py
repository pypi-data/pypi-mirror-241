
#%%
import numpy as np
import networkx as nx
from sevenbridges.graphcreator import graph_generator

latitude_longitude_data = np.array([
    [40.09068,116.17355],
     [40.00395,116.20531],
     [39.91441,116.18424],
     [39.81513,116.17115],
     [39.742767,116.13605],
     [39.987312,116.28745],
     [39.98205,116.3974],
     [39.95405,116.34899],
])

data_in_radians = np.radians(latitude_longitude_data)
n_clusters = 3

generator = graph_generator()
generator.kmeans(latitude_longitude_data, n_clusters)

adj = generator.networkx_graph
print(nx.to_numpy_array(generator.networkx_graph))


generator.create_gabriel_graph(latitude_longitude_data)
print(nx.number_of_nodes(generator.networkx_graph))
print(nx.number_of_edges(generator.networkx_graph))

print(nx.to_numpy_array(generator.networkx_graph))

# plt.scatter(latitude_longitude_data[:, 0], latitude_longitude_data[:, 1])
# for edge in edges:
    # p1, p2 = latitude_longitude_data[edge[0]], latitude_longitude_data[edge[1]]
    # plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-')
# plt.show()

generator.knn(latitude_longitude_data,3)
print(nx.number_of_nodes(generator.networkx_graph))
print(nx.number_of_edges(generator.networkx_graph))

print(nx.to_numpy_array(generator.networkx_graph))

#%%