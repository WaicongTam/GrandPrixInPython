class Driver:  
    def __init__(self, newName = "Default Name", newRanking = 1, newSkill = "Default Skill", newEligibility = True, newAccumulatedScore = 0, newAccumulatedTime = 0, newTyre = "Dry"):
        self.name = newName
        self.ranking = newRanking
        self.skill = newSkill
        self.eligibleToRace = newEligibility
        self.accumulatedScore = newAccumulatedScore
        self.accumulatedTime = newAccumulatedTime
        self.tyre = newTyre
    
    def displayDriver(self):
        info = self.name + "," + str(self.ranking) + "," + self.skill + "," + str(self.eligibleToRace) + "," + \
            str(self.accumulatedScore) + "," + str(self.accumulatedTime) + "," + self.tyre
        return info
    
    def getAccumulatedScore(self):
        return self.accumulatedScore

    def getAccumulatedTime(self):
        return self.accumulatedTime
    
    def getEligibility(self):
        return self.eligibleToRace
    
    def getName(self):
        return self.name

    def getRanking(self):
        return self.ranking

    def getSkill(self):
        return self.skill
    
    def getTyre(self):
        return self.tyre
    
    def increaseAccumulatedScore(self, increment):
        self.accumulatedScore += increment
    
    def increaseAccumulatedTime(self, increment):
        self.accumulatedTime += increment
    
    def setAccumulatedScore(self, newAccumulatedScore):
        if validAccumulatedScore(newAccumulatedScore):
            self.accumulatedScore = newAccumulatedScore
            return True
        else:
            return False
    
    def setAccumulatedTime(self, newAccumulatedTime):
        if validAccumulatedTime(newAccumulatedTime):
            self.accumulatedTime = newAccumulatedTime
            return True
        else:
            return False
    
    def setEligibility(self, newEligibility):
        self.eligibleToRace = newEligibility
    
    def setName(self, newName):
        if validName(newName):
            self.name = newName
            return True
        else:
            return False
    
    def setRanking(self, newRanking):
        if validRanking(newRanking):
            self.ranking = newRanking
            return True
        else:
            return False

    def setSkill(self, newSkill):
        self.skill = newSkill
    
    def setTyre(self, newTyre):
        if validTyre(newTyre):
            self.tyre = newTyre
            return True
        else:
            return False


def validAccumulatedScore(newAccumulatedScore):
    if newAccumulatedScore < 0:
        return False
    else:
        return True

def validAccumulatedTime(newAccumulatedTime):
    if newAccumulatedTime < 0:
        return False
    else:
        return True

def validName(newName):
    if len(newName) == 0:
        return False
    else:
        return True

def validRanking(newRanking):
    if newRanking < 1:
        return False
    else:
        return True

def validSkill(newSkill):
    skillLower = newSkill.lower()
    if skillLower != "overtaking" or skillLower != "cornering" or skillLower != "braking":
        return False
    else:
        return True

def validTyre(newTyre):
    if newTyre.lower() != "dry" or newTyre.lower != "wet":
        return False
    else:
        return True