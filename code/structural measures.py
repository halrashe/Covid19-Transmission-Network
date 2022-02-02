##############################################################

##### Author: Hend Alrasheed     #####
##### Last updated: Jan 10, 2022 #####

## This work is associated with the paper: City Transmission
## Network of COVID-19 in Saudi Arabia

##############################################################


import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
import scipy
import community
import csv
#-----------------------------------------------------------

def analyze_tree(node):

    print 'This is central node: ', node

    T = nx.bfs_tree(G, source=node)

    print 'size: ', len(T)
    print 'diam: ', nx.diameter(T.to_undirected())
    print 'centroid: ', nx.center(T.to_undirected())
    print 'height: ', tree_height(T,node)
    
    print '-----------------------------------'
    print 'Degree centrality:'
    print sorted(T.degree, key=lambda x: x[1], reverse=True)   
    print '-----------------------------------\n'

    print 'Betweenness centrality:'
    print nx.betweenness_centrality(T)

    print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
    print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n'

#-----------------------------------------------------------    
    
def tree_height(T,i):

    m = 0
    for node in T.nodes():
        sh = nx.shortest_path_length(G, source=i, target=node)
        if m < sh:
           m = sh 

    return m    
#-----------------------------------------------------------
    
def get_central_nodes():
    cnt = 0
    for n in G.node():
        if G.node[n]['isSource'] == 'yes':
            cnt=cnt+1
            analyze_tree(n)

    print '# of central nodes: ', cnt    

#-----------------------------------------------------------

def print_trees():

    for n in G.node():
        if G.node[n]['isSource'] == 'yes':
           print 'central node: ', n
           T = nx.bfs_tree(G, source=n)
           print T.node()
           print '========================\n'           

#-----------------------------------------------------------
    
G = nx.read_edgelist('edges.txt', create_using=nx.DiGraph())
nx.set_node_attributes(G, '', name='label')
nx.set_node_attributes(G, '', name='govn')
nx.set_node_attributes(G, '', name='isSource')

print '|V| = ', len(G)
print '|E| = ', G.number_of_edges()


with open('nodes.csv', 'r') as file:
     reader = csv.reader(file)
     for row in reader:
           G.node[row[0]]['label'] = row[1]
           G.node[row[0]]['govn'] = row[2]
           G.node[row[0]]['isSource'] = row[3]



print_trees()
#get_central_nodes()



