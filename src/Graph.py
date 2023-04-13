from Node import *
import networkx as nx
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
    def normalizeGraph(self):
        graph = nx.Graph()
        for i in range(len(self.getListNode())): 
            graph.add_node(i, pos=(self.getNode(i).getCoordinate()[0], self.getNode(i).getCoordinate()[1]))
        for j in range(len(self.getListNode())):
            for k in range(len(self.getListNode())):
                if(self.getAdjMatrix()[j][k]!=0):
                    graph.add_edge(j, k, weight = float(self.getAdjMatrix()[j][k]) )
        return graph

    def drawGraph(self,outputName:str):
        graph = self.normalizeGraph()
        pos=nx.get_node_attributes(graph,'pos')
        nx.draw(graph,pos,with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.savefig(outputName)
        plt.show()
 
    def drawGraphColor(self,Path:list(int)):
        graph = self.normalizeGraph()
        pos=nx.get_node_attributes(graph,'pos')
        nx.draw(graph,pos,with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        listedge = []
        for i in range(len(Path)-1):
            edge = (Path[i],Path[i+1])
            listedge.append(edge)
        nx.draw_networkx_edges(graph,pos,edgelist = listedge,edge_color="tab:red")
        
    def visualize(self, output_filename:str):
        g = nx.Graph()
        adjMatrix = self.getAdjMatrix()
        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix[i])):
                if(adjMatrix[i][j] != 0):
                    g.add_edge(i, j)
        nx.draw(g, with_labels= True)
        plt.savefig(output_filename)
        plt.show()    
