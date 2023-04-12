class LinkedNode():
    def __init__(self,currentNode:int,parentNode=None, nodeCost=0):
        self.__currentNodeName = currentNode
        self.__parentNodeName = parentNode
        self.__nodeCost = nodeCost

    def getCurrentNodeName(self) -> int:
        return self.__currentNodeName

    def getParentNodeName(self) -> int:
        return self.__parentNodeName

    def getNodeCost(self) -> float:
        return self.__nodeCost

    def setCurrentNodeName(self, currentNodeName):
        self.__currentNodeName = currentNodeName

    def setParentNodeName(self, parentNodeName):
        self.__parentNodeName = parentNodeName

    def setNodeCost(self, nodeCost):
        self.__nodeCost = nodeCost

    def __lt__(self, other):
        return (self.getNodeCost() < other.getNodeCost())
