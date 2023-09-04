#Create a random undirected graph G with more then 5 nodes. 

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() 
G = nx.gnm_random_graph(n=10, m=20)

# Draw
 
nx.draw(G, with_labels=True, node_size=350, node_shape= 'o', 
        node_color=[0.8,0.7, 0.9], font_size=10, font_color='blue', 
        width = 2.4, style = 'dotted', font_weight='normal')

plt.show()
