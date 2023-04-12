from Coordinate import *
from math import *
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

    def haversine(self, node2, radius = 6371):
        lat1 = radians(self.getCoordinate().getLatitude())
        lat2 = radians(node2.getCoordinate().getLatitude())
        dLat = radians(lat2 - lat1)
        dLon = radians(node2.getCoordinate().getLongitude() - self.getCoordinate().getLongitude())
        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))
        distance = radius * c
        return distance

    def __str__(self):
        return "Node " + self.__name.__str__() + ": " + self.__coordinate.__str__()

    def __eq__(self, other):
        return ((self.getName() == other.getName()) and (self.getCoordinate() == other.getCoordinate()))

# # Test
# p1 = Coordinate(1.3087,2.9104)
# self = Node(1,p1)
# p2 = Coordinate(1.3087,2.9104)
# node2 = Node(1,p2)
# print(self)
# print(node2)
# if (self == node2):
#     print("node 1 sama dengan node 2")
