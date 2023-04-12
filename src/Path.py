from LinkedNode import *
from Graph import *
import heapq
from math import *
import copy

def haversine(node1:Node, node2:Node, radius = 6371):
        lat1 = radians(node1.getCoordinate().getLatitude())
        lat2 = radians(node2.getCoordinate().getLatitude())
        dLat = radians(lat2 - lat1)
        dLon = radians(node2.getCoordinate().getLongitude() - node1.getCoordinate().getLongitude())
        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))
        distance = radius * c
        return distance

class Path:
    def __init__(self, graph: Graph, startNode: LinkedNode, goalNode: LinkedNode):
        self.__graph = graph
        self.__startNode = startNode
        self.__goalNode = goalNode
        self.__expandNode = startNode
        self.__resultPath = []

    def getGraph(self) -> Graph:
        return self.__graph

    def getExpandNode(self) -> LinkedNode:
        return self.__expandNode
    
    def setExpandNodeCurrent(self, currentNode: Node):
        self.__expandNode = currentNode

    def uniformCostSearch(self):
        liveNodes = []
        heapq.heappush(liveNodes, self.__startNode)

        visitedNodes = set()

        while (len(liveNodes) > 0):
            self.__expandNode = heapq.heappop(liveNodes)

            if(self.getExpandNode().getCurrentNode().getName() == self.__goalNode.getName()):
                while(self.getExpandNode().getCurrentNode().getName() != self.__startNode.getName()):
                    self.__resultPath.append(self.getExpandNode().getCurrentNode().getNumber())
                    tempNode = self.getExpandNode().getParentNode()
                    self.setExpandNodeCurrent(tempNode)
                self.__resultPath.append(self.getExpandNode().getCurrentNode().getName())
                self.__resultPath.reverse()
                return self.__displayPath()

            visitedNodes.add(self.getExpandNode().getCurrentNode().getName())

            for i in range(len(self.getGraph().getAdjMatrix())):
                if((self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNode().getName()][i] != 0) and i not in visitedNodes):
                    newCost = self.getExpandNode().getNodeCost() + self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNode().getName()][i]
                    newLiveNode = LinkedNode(i,self.getGraph().getNode(i).getCoordinate(),self.getGraph().getNode(i),self.getExpandNode().getCurrentNode(),newCost)
                    heapq.heappush(liveNodes, newLiveNode)
        return self.__displayPathNotFound()

    def aStar(self):
        liveNodes = []
        start = copy.deepcopy(self.__startNode)
        start.setNodeCost(haversine(start.getCurrentNode(), self.__goalNode.getCurrentNode()))
        heapq.heappush(liveNodes, start)

        visitedNodes = set()

        while (len(liveNodes) > 0):
            self.__expandNode = heapq.heappop(liveNodes)

            if(self.getExpandNode().getCurrentNode().getName() == self.__goalNode.getName()):
                while(self.getExpandNode().getCurrentNode().getName() != self.__startNode.getName()):
                    self.__resultPath.append(self.getExpandNode().getCurrentNode().getName())
                    tempNode = self.getExpandNode().getParentNode()
                    self.setExpandNodeCurrent(tempNode)
                self.__resultPath.append(self.getExpandNode().getCurrentNode().getName())
                self.__resultPath.reverse()
                return self.__displayPath()

            visitedNodes.add(self.getExpandNode().getCurrentNode().getName())

            for i in range(len(self.getGraph().getAdjMatrix())):
                if((self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNode().getName()][i] != 0) and i not in visitedNodes):
                    newCost = self.getExpandNode().getNodeCost() + self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNode().getName()][i] + haversine(self.getGraph().getAdjMatrix()[self.getExpandNode().getCurrentNode().getName()][i], self.__goalNode.getCurrentNode())
                    newLiveNode = LinkedNode(i,self.getGraph().getNode(i).getCoordinate(),self.getGraph().getNode(i),self.getExpandNode().getCurrentNode(),newCost)
                    heapq.heappush(liveNodes, newLiveNode)
        return self.__displayPathNotFound()
        
    
    def __displayPath(self):
        print("Lintasan ditemukan")
        print(self.__resultPath)

    def __displayPathNotFound(self):
        print("Tidak ada lintasan dari simpul asal ke simpul tujuan")
