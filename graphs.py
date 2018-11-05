# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt

print("Reading graph....")

#Read from txt    
g = nx.read_edgelist('facebook_combined.txt', create_using = nx.Graph(), nodetype = int)
print("Graph loaded!")
print(nx.info(g))
print("-----------------------\n")


print("Drawing graph..")
#Drawing
plt.figure(figsize = (5, 5))
nx.draw(g, with_labels=True)
plt.show()