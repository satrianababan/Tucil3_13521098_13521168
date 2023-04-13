from Node import *
import networkx as nx
# from pyvis.network import Network
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
    # def draw_graph_koor(graph):
    #     pos=nx.get_node_attributes(graph,'pos')
    #     nx.draw(graph,pos,with_labels=True, font_weight='bold')
    #     labels = nx.get_edge_attributes(graph, 'weight')
    #     nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    def drawGraph(self):
        graph = self.normalizeGraph()
        pos=nx.get_node_attributes(graph,'pos')
        nx.draw(graph,pos,with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.show()
    # def draw_graph_koor_color(graph,hasil,nama):
        # pos=nx.get_node_attributes(graph,'pos')
        # nx.draw(graph,pos,with_labels=True, font_weight='bold')
        # labels = nx.get_edge_attributes(graph, 'weight')
        # nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        # listedge = []
        # for i in range(len(hasil)-1):
        #     edge = (nama[hasil[i]],nama[hasil[i+1]])
        #     listedge.append(edge)
        # nx.draw_networkx_edges(graph,pos,edgelist = listedge,edge_color="tab:red")
    def drawGraphColor(self,Path):
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
        
    def visualize(self, output_filename):
        # g = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
        g = nx.Graph()
        # listNode = self.getListNode()
        # for i in range(len(lisNode)):
            # g.add_node(i, label=lisNode[i].getName())
        # g.add_nodes(graph.nodes())
        # g.add_edges()
        adjMatrix = self.getAdjMatrix()
        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix[i])):
                if(adjMatrix[i][j] != 0):
                    g.add_edge(i, j)
        nx.draw(g, with_labels= True)
        # plt.savefig(output_filename)
        plt.show()    
