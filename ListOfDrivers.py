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

    def resetAccumulatedScore(self):
        for i in self.drivers:
            i.setAccumulatedScore = 0
    
    def resetAcuumulatedTime(self):
        for i in self.drivers:
            i.setAccumulatedTime = 0

    def resetEligilibility(self):
        for i in self.drivers:
            i.setEligibility = True
    
    def restTyres(self):
        for i in self.drivers:
            i.setTyre = "Dry"
    
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
        self.drivers = sorted(self.drivers, key=lambda driver: driver.getAccumulatedScore())
    
    def sortByTime(self):
        self.drivers = sorted(self.drivers, key=lambda driver: driver.getAccumulatedTime())