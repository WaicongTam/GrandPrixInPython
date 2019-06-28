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

    def setDriver(self, index, newName, newRanking, newSkill, newEligibility, newAccumulatedScore, newAccumulatedTime, newTyre):
        flag = True
        try:
            flag = flag and self.drivers[index].setName(newName)
            flag = flag and self.drivers[index].setName(newRanking)
            flag = flag and self.drivers[index].setName(newSkill)
            flag = flag and self.drivers[index].setName(newEligibility)
            flag = flag and self.drivers[index].setName(newAccumulatedScore)
            flag = flag and self.drivers[index].setName(newAccumulatedTime)
            flag = flag and self.drivers[index].setName(newTyre)
        except:
            flag = False
        return flag
    
    def setDrivers(self, newDrivers):
        self.drivers = newDrivers

    def sortByScore(self):
        self.drivers = sorted(drivers, key = Driver.getAccumulatedScore)
    
    def sortByTime(self):
        self.drivers = sorted(drivers, key = Driver.getAccumulatedTime)


