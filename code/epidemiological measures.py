##############################################################

##### Author: Hend Alrasheed     #####
##### Last updated: Jan 10, 2022 #####

## This work is associated with the paper: City Transmission
## Network of COVID-19 in 1Saudi Arabia

##############################################################


import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
import scipy
import community
import csv
#-----------------------------------------------------------

def analyze_chains(node):

    print 'This is central node: ', node
    print '# of chains: ', len(list(G.neighbors(node)))

    maximum = total = 0.0
    for n in G.neighbors(node):
        #chain sizes
        cs = len(list(nx.bfs_tree(G, source=n)))
        print 'chain size: ', cs
        if cs > maximum:
           maximum = cs
        total = total + cs

        #maximum length of chains
        #diam = nx.diameter(T.to_undirected())
        print 'max length of chains: ', max_length_of_chains(n)

    print '***'
    if len(list(G.neighbors(node))) > 0:
       print 'average chain size: ', total/len(list(G.neighbors(node)))
    else:
       print 'average chain size: 0'


      

    print '-----------------------------------\n'

#-----------------------------------------------------------
    
def max_length_of_chains(i):

    T = nx.bfs_tree(G, source=i)

    m = 0
    for node in T.nodes():
        sh = nx.shortest_path_length(G, source=i, target=node)
        if m < sh:
           m = sh 

    return m+1    
#-----------------------------------------------------------
    
def get_central_nodes():
    cnt = 0
    for n in G.node():
        if G.node[n]['isSource'] == 'yes':
            cnt=cnt+1
            analyze_chains(n)

    print '# of central nodes: ', cnt    

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

get_central_nodes()



