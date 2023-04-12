from Node import *
from typing import Any

class LinkedNode(Node):
    def __init__(self, name:int, coordinate: Coordinate, currentNode:Node, parentNode:Node, nodeCost=0):
        super().__init__(name,coordinate)
        self.__currentNode = currentNode
        self.__parentNode = parentNode
        self.__nodeCost = nodeCost

    def getCurrentNode(self) -> Any:
        return self.__currentNode

    def getParentNode(self) -> Any:
        return self.__parentNode

    def getNodeCost(self) -> float:
        return self.__nodeCost

    def setCurrentNode(self, currentNode):
        self.__currentNode = currentNode

    def setParentNode(self, parentNode):
        self.__parentNode = parentNode

    def setNodeCost(self, nodeCost):
        self.__nodeCost = nodeCost

    def __lt__(self, other):
        return (self.getNodeCost() < other.getNodeCost())
