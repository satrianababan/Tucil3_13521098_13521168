from Coordinate import *

class Node:
    def __init__(self,name,coordinate=None):
        self.__name = str(name)
        self.__coordinate = coordinate
    
    def getName(self):
        return self.__name

    def getCoordinate(self):
        return self.__coordinate

    def setCoordinate(self,coordinate):
        self.__coordinate = coordinate
    
    def __str__(self):
        return "Node " + self.__name + ": " + self.__coordinate.__str__()
    
# Test
# p1 = Coordinate(1.3,2.9)
# node1 = Node(1,p1)
# print(node1)