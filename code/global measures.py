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
import collections
from scipy import stats
#-----------------------------------------------------------


def degree_distribution():

    
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    #print "Degree sequence", degree_sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    freq = [float(x) / len(G) for x in cnt]

    mean = np.mean(deg)
    median = np.median(deg)
    mode = stats.mode(deg)
    mx = max(deg)
    mn = min(deg)
     

    print 'stats of degree: ', mean, median, mode, mx, mn, np.percentile(deg, [25]), np.percentile(deg, [75])

    fig, ax = plt.subplots()
    plt.bar(deg, freq, width=0.80, color='darkgrey')
    #plt.scatter(deg, freq)
    
    #plt.title("Degree Histogram")
    plt.ylabel("Frequency")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)

    plt.show()

#-----------------------------------------------------------

def distance_matrix():

    matrix = [[]]
    matrix = np.zeros((len(G), len(G)))
    x=y=0

    for i in G.nodes():
        for j in G.nodes():
            try:
               val = nx.shortest_path_length(G.to_undirected(), source=i, target=j)
               #print val
               matrix[x][y] = val
               y=y+1
               break
            except:
               print 'path not found' 
        x=x+1

    fig, ax = plt.subplots()
    im = ax.imshow(matrix, interpolation='none', cmap=plt.cm.Greens)

    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Distance', rotation=-90, va="bottom")
    
    #ax.set_xticks(np.arange(len(g)))
    #ax.set_yticks(np.arange(len(g)))
    plt.gca().invert_yaxis()
    ax.set_title("Node similarity")
    #fig.tight_layout()
    plt.show()

#-----------------------------------------------------------

def check_edges():

    a=b=0
    
    for u,v,data in G.edges(data=True):

        if G.nodes[u]['govn'] == G.nodes[v]['govn']:
            a=a+1
        else:
            b=b+1

    print 'Edges connecting citities in the same region: ', a
    print 'Edges connecting citities in the diff region: ', b

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

degree_distribution()

#check_edges()
#print nx.eccentricity(G.to_undirected())
#distance_matrix()
#sorted_cities = sorted(nx.closeness_centrality(G).items(), key = lambda kv: kv[1])
#print sorted_cities



