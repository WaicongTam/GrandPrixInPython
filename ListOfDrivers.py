import Driver
class ListOfDrivers:
    def __init__(self, newDrivers = []):
        self.drivers = newDrivers

    def __str__(self):
        info = ""
        for i in self.drivers:
            info += str(i)
        return info

    def getDriver(self, index):
        try:
            return self.drivers[index]
        except IndexError:
            return Driver.Driver()

    def getDrivers(self):
        return self.drivers

