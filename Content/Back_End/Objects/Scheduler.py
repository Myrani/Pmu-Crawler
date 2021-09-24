from Content.Back_End.Objects.WorkerSignals import SchedulerSignals, WorkerSignalsExtracter
import sched
import time
import datetime
from PySide2 import QtCore
from PySide2.QtCore import SIGNAL, QDateTime, QEventLoop, QObject, QThread,QTimer, Qt

class Scheduler():

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

        for race in self.parent.pingList15minutes:
            self.add15MinutesBeforePing(race)
            
 
        for race in self.parent.pingList30minutes:
            self.add30MinutesBeforePing(race)

        for race in self.parent.pingList60minutes:
            self.add1HourBeforePing(race)
 
        self.showQueue()
    ### Add timers to a function 
    
    #Add a ping 1 Hour before launch 
    def add1HourBeforePing(self,race):
        time = datetime.datetime(self.year, self.month, self.day, race.getHour(),race.getMinutes(), 0,0).timestamp()-3600  - QDateTime.currentDateTime().toSecsSinceEpoch()
   
        self.pingIn_Seconds(time,race)


    # Add a ping 30 minutes before launch
    def add30MinutesBeforePing(self, race):    
        time = datetime.datetime(self.year, self.month, self.day, race.getHour(),race.getMinutes(), 0,0).timestamp()-1800  - QDateTime.currentDateTime().toSecsSinceEpoch()
        self.pingIn_Seconds(time,race)

    # Add a ping 15 minutes before launch
    def add15MinutesBeforePing(self,race):
        time = datetime.datetime(self.year, self.month, self.day, race.getHour(),race.getMinutes(), 0,0).timestamp()-900  - QDateTime.currentDateTime().toSecsSinceEpoch()
        self.pingIn_Seconds(time,race)

    def getRaceResults(self,hours,minutes,raceUrl):
        self.scheduler.enterabs(datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-3600, 1, self.parent.startPreciseRaceReExtraction, argument=1,kwargs=raceUrl)
    
    def pingIn_Seconds(self,seconds,race):
        print(race)
        print(race.getUrl())
        print(self.parent.startCrawlingReExtraction)
        timer = QtCore.QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(lambda:self.parent.startCrawlingReExtraction(race))
        print(QDateTime.currentDateTime().addSecs(5).toMSecsSinceEpoch() - QDateTime.currentDateTime().toMSecsSinceEpoch())
        timer.start(QDateTime.currentDateTime().addSecs(5).toMSecsSinceEpoch() - QDateTime.currentDateTime().toMSecsSinceEpoch())
        self.timerList.append(timer)

    def showQueue(self):
        for timer in self.timerList:
            print(timer)

    