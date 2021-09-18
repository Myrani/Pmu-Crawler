class Race():
    def __init__(self,raceName,raceData):
        self.rawdata = raceData
        self.name = raceName
        self.timer = raceName[0:6]
        self.hour = int(raceName[0:3])
        self.minutes = int(raceName[4:6])
        self.url = raceData["url"]

    def getUrl(self):
        return self.url

    def getTimer(self):
        return self.timer
    
    def getName(self):
        return self.name

    def getRawData(self):
        return self.rawdata

    def getHour(self):
        return self.hour
    
    def getMinutes(self):
        return self.minutes