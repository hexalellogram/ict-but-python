class Car:
    def __init__(self, odometerReading):
        self.__myStartMiles__ = int(odometerReading)
        self.__myEndMiles__ = int(odometerReading)
        self.__myGallonsUsed__ = 0

    def fillUp(self, odometerReading, gallons):
        self.__myEndMiles__ = int(odometerReading)
        self.__myGallonsUsed__ = self.__myGallonsUsed__ + float(gallons)

    def calculateMPG(self):
        totalMiles = self.__myEndMiles__ - self.__myStartMiles__
        return totalMiles / self.__myGallonsUsed__

    def resetMPG(self):
        self.__myGallonsUsed__ = 0
        self.__myStartMiles__ = self.__myEndMiles__

    def getCurrentMileage(self):
        return self.__myEndMiles__
