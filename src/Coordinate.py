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
    
    def __eq__(self, other):
        return ((self.getLatitude() == other.getLatitude()) and (self.getLongitude() == other.getLongitude()))

# # Test
# p1 = Coordinate()
# print(p1.getLatitude())
# print(p1.getLongitude())
# p1.setLatitude(1.654789)
# p1.setLongitude(1.076)
# print(p1)
# p2 = Coordinate(1.654789,1.076)
# print(p2)
# if (p1 == p2):
#     print("p1 sama dengan p2")