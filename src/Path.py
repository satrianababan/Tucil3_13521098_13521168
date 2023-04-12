from Node import *
from Graph import *
import heapq

class Path:
    def __init__(self,graph:Graph,startNode:Node,goalNode:Node):
        self.__graph = graph
        self.__listNodes = []
        self.__startNode = startNode
        self.__goalNode = goalNode
        self.__currentNode = None
        self.__pathCost = 0
    
    def getCurrentNode(self):
        return self.__currentNode
    
    def getParentNode(self):
        return self.__parentNode

    def getGraph(self):
        return self.__graph
    
    def getListNodes(self):
        return self.__listNodes
    
    def __lt__(self,other):
        return (self.__pathCost < other.__pathCost)
    
    def uniformCostSearch(self):
        liveNodes = []
        heapq.heappush(liveNodes, self.__startNode)

        visitedNodes = set()

        while (len(liveNodes) > 0):
            self.__currentNode = heapq.heappop(liveNodes)

            if(self.__currentNode == self.__goalNode):
                while(self.__currentNode):
                    self.__listNodes.append(self.__currentNode)
                    self.__currentNode = self.__parentNode
                self.__listNodes.reverse()
                return self.__displayPath()
            
            visitedNodes.add(self.getCurrentNode().getName())

            for i in range(len(self.__graph)):
                if((self.__graph.getAdjMatrix()[self.getCurrentNode().getName()][i] != 0) 
                   and i not in visitedNodes):
                    self.__pathCost = self.__pathCost + self.getGraph().getAdjMatrix()[self.getCurrentNode().getName()][i]
                    newLiveNode = Node(i,None)
                    heapq.heappush(liveNodes,newLiveNode)
        return self.__displayPathNotFound
    
    def __displayPath(self):
        print("Lintasan terpendek adalah " + self.getListNodes())

    def __displayPathNotFound(self):
        print("Tidak ada lintasan dari simpul asal ke simpul tujuan")
        
