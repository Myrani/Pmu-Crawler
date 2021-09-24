from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import sys
import os
import gc

from PySide2.QtCore import QObject, QThread,QEventLoop,QTimer,QProcess
from Content.Back_End.Objects.WorkerSignals import WorkerSignalsExtracter, WorkerSignalsReExtracter

class UrlReExtracterQThread(QObject):
    
    def __init__(self, race,parent=None):
        super( UrlReExtracterQThread, self).__init__(parent=parent)
        self.race = race
        self.url = race.getUrl()
        self.parent = parent
        print("Moi :",self)
        self.signals = WorkerSignalsReExtracter()
    
    def resource_path(self,relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("Content\\Back_End\\Crawlers\\") 
            #"." 
            #"Content\\Back_End\\Crawlers\\"
        return os.path.join(base_path, relative_path)


    def run(self):
        #Instatiation du crawler
        self.participantDict = {}
        self.currentRaceName = ""
        
        self.fireFoxOptions = Options()
        self.fireFoxOptions.add_argument("--headless")

        self.driver = webdriver.Firefox(options=self.fireFoxOptions,executable_path=self.resource_path('geckodriver.exe'))
        
        try:
            self.driver.get(self.url)
    
            self.html = self.driver.execute_script("return document.documentElement.outerHTML")
            self.soup = BeautifulSoup(self.html, 'html.parser')



            #Trouve le nom de la course actuelle
            for raceName in self.soup.findAll("h3",{"class" : "reunion-description"}):
                self.currentRaceName = raceName.text


            # Extrait les participants
            self.naming = True
            self.currentName = ""
            for tab in self.soup.findAll("table",  {"class":["table", "condensed", "striped", "ca" ]}):
                for participant in tab.findAll("tr"):
                    for spec in participant.findAll("td"):
                        try:
                            if self.naming :
                                currentName = str(spec.text).replace('\n','').replace('\t','').replace(' ','')    
                                self.participantDict[currentName] = []
                                self.naming = False
                            else:
                                self.participantDict[currentName].append(str(spec.text).replace('\n','').replace('\t','').replace(' ',''))
                        except Exception as e:
                            print(e)
                            pass
                    self.naming = True


        except Exception as e:
            self.driver.quit()        
        
        
        #Les renvoies

        self.participantDict = {key:value for key, value in self.participantDict.items() if len(value) > 5}
        self.participantDict["url"] = self.url 
        self.signals.finished.emit({self.currentRaceName:self.participantDict})
        
        self.driver.quit()
        
        gc.collect()
        print("Done",self)