import sched
import time
import datetime


class Scheduler():

    def __init__(self,parent=None):
        # Parent, duh
        self.parent = parent 

        # Current time variables
        self.year = datetime.datetime.today().year
        self.month = datetime.datetime.today().month
        self.day = datetime.datetime.today().day

        # Scheduler entity
        self.scheduler = sched.scheduler(time.time, time.sleep)


    ### Add timers to a function 
    
    #Add a ping 1 Hour before launch 
    def add1HourBeforePing(self,hours,minutes,raceUrl):
        self.scheduler.enterabs(datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-3600, 1, self.parent.startPreciseExtraction, argument=(raceUrl))
    
    # Add a ping 30 minutes before launch
    def add30MinutesBeforePing(self,hours,minutes,raceUrl):    
        self.scheduler.enterabs(datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-1800, 1, self.parent.startPreciseExtraction, argument=(raceUrl))
    
    # Add a ping 15 minutes before launch
    def add15MinuntesBeforePing(self,hours,minutes,raceUrl):
        self.scheduler.enterabs(datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-900, 1, self.parent.startPreciseExtraction, argument=(raceUrl))    
    
    def getRaceResults(self,hours,minutes,raceUrl):
        self.scheduler.enterabs(datetime.datetime(self.year, self.month, self.day, hours, minutes, 0,0).timestamp()-3600, 1, self.parent.startPreciseExtraction, argument=(raceUrl))