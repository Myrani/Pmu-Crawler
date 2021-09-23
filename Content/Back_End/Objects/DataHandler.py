import sys
import os
from datetime import date
import pickle
from Content.Back_End.Objects.Race import Race 

class DataHandler():
    
    def __init__(self,parent=None):
        self.currentDate = date.today().strftime("%d/%m/%Y")
        self.parent = parent

    def resource_path(self,relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".") 
            #"." 
            #"Content\\Back_End\\Saves\\"
        return os.path.join(base_path, relative_path)

    def fileCreation(self):
        with open(self.resource_path('save.pkl'), 'wb') as savefile:
            pickle.dump({"Jourdui":{"Course1":"Value1","Course2":"value2"}} ,savefile)

    def loadFile(self):
        try :
            with open(self.resource_path('save.pkl'), 'rb') as savefile:
                self.parent.racesFile = pickle.load(savefile)
        except Exception :
            self.fileCreation()
            self.loadFile()

    def saveCurrentResults(self):
        self.parent.racesFile[self.currentDate] = self.parent.racesDone
        with open(self.resource_path('save.pkl'), 'wb') as savefile:
            pickle.dump(self.parent.racesFile ,savefile)


    # returns data from current Scheduler day 

    def getDayData(self):
        try:
            return self.parent.racesFile[self.currentDate]
        except Exception as e:
            return {}


    def generateRacesListFromDayData(self):
        racelist = []
        for name,data in self.getDayData().items():
            racelist.append(Race(name,data))

        return racelist

    ### Self care function 

    def showCurrentData(self):
        for key,value in self.parent.racesFile.items():
            print(key,value)

    def showSavedData(self):
        with open(self.resource_path('save.pkl'), 'rb') as savefile:
            for date,results in pickle.load(savefile).items():
                print(date)
                for key,value in results.items():
                    print(key,value)