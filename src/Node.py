from Coordinate import *
class Node:
    def __init__(self, name: int, coordinate:Coordinate):
        self.__name = name
        self.__coordinate = coordinate

    def getName(self):
        return self.__name

    def getCoordinate(self):
        return self.__coordinate

    def setCoordinate(self, coordinate):
        self.__coordinate = coordinate

    def __str__(self):
        return "Node " + self.__name.__str__() + ": " + self.__coordinate.__str__()

    def __eq__(self, other):
        return ((self.getName() == other.getName()) and (self.getCoordinate() == other.getCoordinate()))

# # Test
# p1 = Coordinate(1.3087,2.9104)
# node1 = Node(1,p1)
# p2 = Coordinate(1.3087,2.9104)
# node2 = Node(1,p2)
# print(node1)
# print(node2)
# if (node1 == node2):
#     print("node 1 sama dengan node 2")
