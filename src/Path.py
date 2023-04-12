from LinkedNode import *
from Graph import *
import heapq
from math import *
import copy
from Utility import *

class Path:
    def __init__(self, graph: Graph, startNode: Node, goalNode: Node):
        self.__graph = graph
        self.__startNode = startNode
        self.__goalNode = goalNode
        self.__expandNode = None
        self.__resultPath = []

    def getGraph(self) -> Graph:
        return self.__graph

    def getStartNode(self) -> Node:
        return self.__startNode
    
    def getGoalNode(self) -> Node:
        return self.__goalNode
    
    def getExpandNode(self) -> LinkedNode:
        return self.__expandNode

    def uniformCostSearch(self):
        liveNodes = []
        self.__expandNode = LinkedNode(self.getStartNode().getName())
        heapq.heappush(liveNodes, self.__expandNode)

        visitedNodes = set()

        while (liveNodes):
            self.__expandNode = heapq.heappop(liveNodes)

            if(self.getExpandNode().getCurrentNodeName() == self.__goalNode.getName()):
                while(self.__expandNode != self.getStartNode().getName()):
                    self.__resultPath.append(self.getExpandNode().getCurrentNodeName())
                    self.__expandNode = self.getExpandNode().getParentNodeName()
                self.__resultPath.append(self.getExpandNode())
                self.__resultPath.reverse()
                return self.__displayPath()

            visitedNodes.add(self.getExpandNode().getCurrentNodeName())

            for i in range(len(self.getGraph().getAdjMatrix())):
                if((self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNodeName()][i] != 0) and i not in visitedNodes):
                    newCost = self.getExpandNode().getNodeCost() + self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNodeName()][i]
                    newLiveNode = LinkedNode(i,self.getExpandNode().getCurrentNodeName(),newCost)
                    heapq.heappush(liveNodes, newLiveNode)
        return self.__displayPathNotFound()

    def aStar(self):
        liveNodes = []
        self.__expandNode = LinkedNode(self.getStartNode().getName())
        self.__expandNode.setNodeCost(haversine(self.getStartNode(), self.getGoalNode()))
        heapq.heappush(liveNodes, self.__expandNode)

        visitedNodes = set()

        while (len(liveNodes) > 0):
            self.__expandNode = heapq.heappop(liveNodes)

            if(self.getExpandNode().getCurrentNodeName() == self.__goalNode.getName()):
                while(self.__expandNode != self.getStartNode().getName()):
                    self.__resultPath.append(self.getExpandNode().getCurrentNodeName())
                    self.__expandNode = self.getExpandNode().getParentNodeName()
                self.__resultPath.append(self.getExpandNode())
                self.__resultPath.reverse()
                return self.__displayPath()

            visitedNodes.add(self.getExpandNode().getCurrentNodeName())

            for i in range(len(self.getGraph().getAdjMatrix())):
                if((self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNodeName()][i] != 0) and i not in visitedNodes):
                    newCost = self.getExpandNode().getNodeCost() + self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNodeName()][i] + haversine(self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNodeName()][i], self.__goalNode)
                    newLiveNode = LinkedNode(i,self.getExpandNode().getCurrentNodeName(),newCost)
                    heapq.heappush(liveNodes, newLiveNode)
        return self.__displayPathNotFound()
        
    
    def __displayPath(self):
        print("Lintasan terpendek adalah ", end="")
        print(self.__resultPath)

    def __displayPathNotFound(self):
        print("Tidak ada lintasan dari simpul asal ke simpul tujuan")
