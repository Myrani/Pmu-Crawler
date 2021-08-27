from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import sys
import os

from PyQt5.QtCore import QThread,QEventLoop,QTimer,QProcess
from Content.Back_End.WorkerSignals import WorkerSignalsExtracter

class UrlExtracterQThread(QProcess):
    
    def __init__(self, url,parent=None):
        super( UrlExtracterQThread, self).__init__()
        self.url = "https://www.genybet.fr" + url
        self.parent = parent
        print("Moi :",self)
        self.signals = WorkerSignalsExtracter()
    
    def resource_path(self,relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("Content\\Back_End\\") 
            #"." 
            #"Content\\Back_End\\"
        return os.path.join(base_path, relative_path)


    def run(self):
        #Instatiation du crawler
        participantDict = {}

        fireFoxOptions = Options()
        fireFoxOptions.add_argument("--headless")

        driver = webdriver.Firefox(options=fireFoxOptions,executable_path=self.resource_path('geckodriver.exe'))
        driver.get(self.url)
    
        html = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(html, 'html.parser')

        #Trouve toutes les courses du jour
        naming = True
        currentName = ""
        for tab in soup.findAll("table",  {"class":["table", "condensed", "striped", "ca" ]}):
            for participant in tab.findAll("tr"):
            
                for spec in participant.findAll("td"):
                    try:
                        if naming :
                            currentName = str(spec.text).replace('\n','').replace('\t','')    
                            participantDict[currentName] = []
                            naming = False
                        else:
                            participantDict[currentName].append(str(spec.text).replace('\n','').replace('\t',''))
                    except Exception as e:
                        print(e)
                        pass

            naming = True
        #Les renvoies

        participantDict = {key:value for key, value in participantDict.items() if len(value) > 5}
        
        self.signals.finished.emit(participantDict)

