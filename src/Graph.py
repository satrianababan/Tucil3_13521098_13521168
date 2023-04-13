from Node import *

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
