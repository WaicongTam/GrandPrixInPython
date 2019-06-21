class Driver:  
    def __init__(self, newName = "Default Name", newRanking = 1, newSkill = "Default Skill", newEligibility = True, newAccumulatedScore = 0, newAccumulatedTime = 0, newTyre = "Dry"):
        self.name = newName
        self.ranking = newRanking
        self.skill = newSkill
        self.eligibleToRace = newEligibility
        self.accumulatedScore = newAccumulatedScore
        self.accumulatedTime = newAccumulatedTime
        self.tyre = newTyre
    
    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6}".format(self.name, self.ranking, self.skill, self.eligibleToRace, self.getAccumulatedScore, self.getAccumulatedTime, self.tyre)
    
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
        try:
            validAccumulatedScore(newAccumulatedScore)
            self.accumulatedScore = newAccumulatedScore
            return True
        except ValueError:
            return False
    
    def setAccumulatedTime(self, newAccumulatedTime):
        try:
            validAccumulatedTime(newAccumulatedTime)
            self.accumulatedTime = newAccumulatedTime
            return True
        except ValueError:
            return False
    
    def setEligibility(self, newEligibility):
        self.eligibleToRace = newEligibility
    
    def setName(self, newName):
        try:
            validName(newName)
            self.name = newName
            return True
        except ValueError:
            return False
    
    def setRanking(self, newRanking):
        try:
            validRanking(newRanking)
            self.ranking = newRanking
            return True
        except ValueError:
            return False

    def setSkill(self, newSkill):
        try:
            validSkill(newSkill)
            self.skill = newSkill
            return True
        except ValueError:
            return False
    
    def setTyre(self, newTyre):
        try:
            validTyre(newTyre)
            self.tyre = newTyre
            return True
        except ValueError:
            return False


def validAccumulatedScore(newAccumulatedScore):
    if newAccumulatedScore < 0:
        raise ValueError("This is a invalid accumulated score!")

def validAccumulatedTime(newAccumulatedTime):
    if newAccumulatedTime < 0:
        raise ValueError("This is a invalid accumulated time!")

def validName(newName):
    if len(newName) == 0:
        raise ValueError("This is a invalid accumulated namee!")

def validRanking(newRanking):
    if newRanking < 1:
        raise ValueError("This is a invalid accumulated ranking!")

def validSkill(newSkill):
    skillLower = newSkill.lower()
    if skillLower != "overtaking" or skillLower != "cornering" or skillLower != "braking":
        raise ValueError("This is a invalid accumulated skill!")

def validTyre(newTyre):
    if newTyre.lower() != "dry" or newTyre.lower != "wet":
        raise ValueError("This is a invalid accumulated tyre!")