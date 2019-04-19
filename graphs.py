# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

print("Reading graph....")

#Read from txt    
g = nx.read_edgelist('amazon_combined', create_using = nx.Graph(), nodetype = int)
print("Graph loaded!")
print(nx.info(g))
print("-----------------------\n")

#detect communities and label nodes
print("detecting communities")
#communities_gen = community.girvan_newman(g)
#top_level_comm = next(communities_gen)

print("Done!")
#Write for gephi
nx.write_gexf(g, "text.gexf")

#DRAWING

'''
#Calculate layout (Slow Part!)
print("Calculating layout..")
sp = nx.spring_layout(g)

print("Drawing graph..")

plt.figure(figsize = (7, 7))
plt.axis('off')
nx.draw(g, with_labels=False, pos=sp, node_size = 20)
plt.show()

'''