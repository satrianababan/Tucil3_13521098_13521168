from Coordinate import *
from math import *
class Node:
    def __init__(self, name: int, coordinate:Coordinate):
        self.__name = name
        self.__coordinate = coordinate

    def getName(self):
        return self.__name
    
    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def setLatitude(self, latitude):
        self.__latitude = latitude
    
    def setLongitude(self, longitude):
        self.__longitude = longitude

    def getCoordinate(self):
        return self.__coordinate

    def setCoordinate(self, coordinate):
        self.__coordinate = coordinate

    def __str__(self):
        return "Node " + self.__name.__str__() + ": " + self.__coordinate.__str__()

    def __eq__(self, other):
        return ((self.getName() == other.getName()) and (self.getCoordinate() == other.getCoordinate()))