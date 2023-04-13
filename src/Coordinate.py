class Coordinate:
    def __init__(self,latitude=0.0,longitude=0.0):
        self.__latitude = latitude
        self.__longitude = longitude
    
    def __str__(self):
        return ("(" + str(self.__latitude) + ", " + str(self.__longitude) + ")")
    
    def __eq__(self, other):
        return ((self.getLatitude() == other.getLatitude()) and (self.getLongitude() == other.getLongitude()))