from Node import *

class Graph:
    def __init__(self,adjMatrix:list(list(float))):
        self.__adjMatrix = adjMatrix
    
    def getAdjMatrix(self):
        return self.__adjMatrix

