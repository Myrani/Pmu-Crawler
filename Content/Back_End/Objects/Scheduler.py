import sched
import time
import datetime
from PySide2 import QtCore
from PySide2.QtCore import QDateTime, QEventLoop, QObject, QThread,QTimer, Qt

class Scheduler(QObject):

    def __init__(self,parent=None):
        # Parent, duh
        self.parent = parent 
    
        # Current time variables
        self.year = datetime.datetime.today().year
        self.month = datetime.datetime.today().month
        self.day = datetime.datetime.today().day
        self.hour = datetime.datetime.today().hour
        self.minutes = datetime.datetime.today().minute


        self.timerList= []

        self.pingIn_Seconds(5,self.parent.startPreciseExtraction,"Ping")
        self.pingIn_Seconds(20,self.parent.startPreciseExtraction,"Pong")
        

    def setup(self):
        
        for race in self.parent.pingList15minutes:
            self.add15MinutesBeforePing(race.getHour(),race.getMinutes(),race.getUrl())
 
        for race in self.parent.pingList30minutes:
            self.add30MinutesBeforePing(race.getHour(),race.getMinutes(),race.getUrl())

        for race in self.parent.pingList60minutes:
            self.add1HourBeforePing(race.getHour(),race.getMinutes(),race.getUrl())
 
        self.showQueue()
    ### Add timers to a function 
    
    #Add a ping 1 Hour before launch 
    def add1HourBeforePing(self,hours,minutes,raceUrl):
        time = datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-3600  - QDateTime.currentDateTime().toSecsSinceEpoch()
        self.pingIn_Seconds(time,self.parent.startPreciseExtraction,raceUrl)


    # Add a ping 30 minutes before launch
    def add30MinutesBeforePing(self,hours,minutes,raceUrl):    
        time = datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-1800  - QDateTime.currentDateTime().toSecsSinceEpoch()
        self.pingIn_Seconds(time,self.parent.startPreciseExtraction,raceUrl)

    # Add a ping 15 minutes before launch
    def add15MinutesBeforePing(self,hours,minutes,raceUrl):
        time = datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-900  - QDateTime.currentDateTime().toSecsSinceEpoch()
        self.pingIn_Seconds(time,self.parent.startPreciseExtraction,raceUrl)

    def getRaceResults(self,hours,minutes,raceUrl):
        self.scheduler.enterabs(datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-3600, 1, self.parent.startPreciseExtraction, argument=1,kwargs=raceUrl)
    
    def pingIn_Seconds(self,seconds,function,raceUrl):
        timer = QtCore.QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(lambda:function(raceUrl))
        timer.start(QDateTime.currentDateTime().addSecs(seconds).toMSecsSinceEpoch() - QDateTime.currentDateTime().toMSecsSinceEpoch())
        self.timerList.append(timer)

    def showQueue(self):
        for timer in self.timerList:
            print(timer)

    