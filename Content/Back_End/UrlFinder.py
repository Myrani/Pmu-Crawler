from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import sys
import os

from PyQt5.QtCore import QThread,QEventLoop,QTimer,QProcess
from Content.Back_End.WorkerSignals import WorkerSignalsFinder

class UrlFinderQThread(QProcess):
    
    def __init__(self, parent=None):
        super(UrlFinderQThread, self).__init__()
        self.parent = parent
        print("Parent !", self.parent.parent())
        self.signals = WorkerSignalsFinder()
    
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
        base_url = "https://www.genybet.fr/"
        liste_des_courses = []

        fireFoxOptions = Options()
        fireFoxOptions.add_argument("--headless")

        driver = webdriver.Firefox(options=fireFoxOptions,executable_path=self.resource_path('geckodriver.exe'))

        driver.get(base_url)
    
        html = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(html, 'html.parser')

        #Trouve toutes les courses du jour
        for champ in soup.findAll("div", {"class": "timeline-container"}):
            for course in champ.findAll("a"):
                try:
                    liste_des_courses.append(str(course.get("href")))
                except Exception as e:
                    print(e)
                    pass
        #Les renvoies
        self.signals.finished.emit(liste_des_courses)
