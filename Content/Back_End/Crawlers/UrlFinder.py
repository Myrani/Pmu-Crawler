
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import sys
import os
import gc

from PySide2.QtCore import QRunnable, QThread,QEventLoop,QTimer,QProcess,QObject
from Content.Back_End.Objects.WorkerSignals import WorkerSignalsFinder

class UrlFinderQThread(QRunnable):
    
    def __init__(self, parent=None):
        super(UrlFinderQThread, self).__init__(parent=parent)
        self.parent = parent
        print("Parent !", self.parent.parent())
        self.signals = WorkerSignalsFinder()
    
    def resource_path(self,relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath("Content\\Back_End\\Crawlers\\") 
            #"." 
            #"Content\\Back_End\\"
        return os.path.join(base_path, relative_path)


    def run(self):
        #Instatiation du crawler
        self.base_url = "https://www.genybet.fr/"
        self.liste_des_courses = []

        self.fireFoxOptions = Options()
        self.fireFoxOptions.add_argument("--headless")

         
        self.driver = webdriver.Firefox(options=self.fireFoxOptions,executable_path=self.resource_path('geckodriver.exe'))
        
        try:
            
            self.driver.get(self.base_url)
            
            html = self.driver.execute_script("return document.documentElement.outerHTML")
            soup = BeautifulSoup(html, 'html.parser')

            #Trouve toutes les courses du jour
            for champ in soup.findAll("div", {"class": "timeline-container"}):
                for course in champ.findAll("a"):
                    try:
                        self.liste_des_courses.append(str(course.get("href")))
                    except Exception as e:
                        print(e)
                        pass
        
        except Exception:   
            self.driver.quit()

        
        #Les renvoies
        self.signals.finished.emit(self.liste_des_courses)

        self.driver.quit()
        gc.collect()
