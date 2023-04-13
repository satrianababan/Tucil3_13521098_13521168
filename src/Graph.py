from Node import *
import networkx as nx
from pyvis.network import Network
from Utility import *
class Graph:
    def __init__(self, nodes, adjMatrix):
        self.__nodes = nodes
        self.__adjMatrix = adjMatrix

    def getNode(self,index:int) -> Node:
        return self.__nodes[index]

    def getAdjMatrix(self):
        return self.__adjMatrix
    
    def getListNode(self):
        return self.__nodes
    
    def displayAdjList(self):
        adjMatrix = self.getAdjMatrix()
        for i in range(len(adjMatrix)):
            print(i, end='')
            for j in range(len(adjMatrix[i])):
                if(adjMatrix[i][j] != 0):
                    print(" --> " + str(j), end = '')
            print()
            
    def visualize(self, output_filename):
        g = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
        lisNode = self.getListNode()
        for i in range(len(lisNode)):
            g.add_node(i, label=lisNode[i].getName())
        # g.add_nodes(graph.nodes())
        # g.add_edges()
        adjMatrix = self.getAdjMatrix()
        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix[i])):
                if(adjMatrix[i][j] != 0):
                    g.add_edge(i, j, value=adjMatrix[i][j])
        g.show(output_filename)
