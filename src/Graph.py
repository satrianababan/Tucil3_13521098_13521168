from Node import *

class Graph:
    def __init__(self, nodes, adjMatrix):
        self.__nodes = nodes
        self.__adjMatrix = adjMatrix

    def getNode(self,index:int) -> Node:
        return self.__nodes[index]

    def getAdjMatrix(self):
        return self.__adjMatrix
