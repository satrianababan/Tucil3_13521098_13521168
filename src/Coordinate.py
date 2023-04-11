class Coordinate:
    def __init__(self,latitude=0.0,longitude=0.0):
        self.__latitude = latitude
        self.__longitude = longitude
    
    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def setLatitude(self, latitude):
        self.__latitude = latitude
    
    def setLongitude(self, longitude):
        self.__longitude = longitude
    
    def __str__(self):
        return ("(" + str(self.__latitude) + ", " + str(self.__longitude) + ")")

# # Test
# p1 = Coordinate()
# print(p1.getLatitude())
# print(p1.getLongitude())
# p1.setLatitude(1)
# p1.setLongitude(1)
# print(p1.getLatitude())
# print(p1.getLongitude())
# p2 = Coordinate(2,2)
# print(p2.getLatitude())
# print(p2.getLongitude())
# print(p2)