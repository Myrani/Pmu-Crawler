from Content.Back_End.UrlExtracter import UrlExtracterQThread
from Content.Back_End.UrlFinder import UrlFinderQThread
from Content.Front_End.Windows.RacesWindow import RacesWindow
from Content.Front_End.Windows.DashboardWindow import DashboardWindow
from Content.Front_End.Windows.CrawlerWindow import CrawlerWindow
from Content.Front_End.Windows.MonitoringWindow import MonitoringWindow

import os
import sys


from PyQt5.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QLabel, QDesktopWidget
from PyQt5.QtCore import QThreadPool, Qt, QPoint
from PyQt5.QtGui import QPixmap



class MainWindow(QMainWindow):
    
    # First window generated, stocks all the long terms variable of the session between different windows
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(10, 10, 1280, 720)
        # Durable variable initialisation 
        self.racesFile = {}
        self.racesLinks = []
        self.racesDone = []
        
        # Window Opacity
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(0.95)
        self.setContentsMargins(0,0,0,0)
        #self.label_background.move(0, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:rgba(0, 0, 0, 1);")

        # Création de la Process Pool 
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(4)

        # Instanciation de l'acceuil
        self.init_Windows()

        self.startDashboardWindow()
    
    def init_Windows(self):
        self.dashboardWindow = False
        self.monitoringWindow = False
        self.crawlerWindow = False
        self.racesWindow = False

        self.lastWindow = ""

        self.windowDict = {"dashboard":self.startDashboardWindow,"crawler":self.startCrawlerWindow,"monitoring":self.startMonitoringWindow,"races":self.startRacesWindow}

    # Dynamic Ressources pathing compatible with PyInstaller
    def resource_path(self,relative_path):
        """ Get the absolute path to the resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".") 
            #"." Penser à Job,Job Processor
            #"Content\\Back_End\\"
        return os.path.join(base_path, relative_path)

    ### Dragable window part
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    #Reachable Functions
    def print1(self,x):
        print(x,1)

    def print2(self,x):
        print(x,2)
   
    ### Windows startup functions

    def startDashboardWindow(self):

        self.dashboardWindow = DashboardWindow(parent=self)
        self.setCentralWidget(self.dashboardWindow)
        self.lastWindow = "dashboard"
        self.show()
   
    def startMonitoringWindow(self):

        self.monitoringWindow = MonitoringWindow(parent=self)
        self.setCentralWidget(self.monitoringWindow)
        self.lastWindow = "monitoring"
        self.show()
    
    def startCrawlerWindow(self):

        self.crawlerWindow = CrawlerWindow(parent=self)
        self.setCentralWidget(self.crawlerWindow)
        self.lastWindow = "crawler"
        self.show()
    
    def startRacesWindow(self):

        self.racesWindow = RacesWindow(parent=self)
        self.setCentralWidget(self.racesWindow)
        self.lastWindow = "races"
        self.show()

    ### Refresh the last windows in case case of content update
    def refreshCurrenWindow(self):
        self.windowDict[self.lastWindow]()


    ### Fonction de lancement des Crawlers web
    def startCrawlingFinder(self):
        self.worker = UrlFinderQThread(parent=self)
        self.worker.signals.finished.connect(self.loadRacesLinks)
        self.threadpool.start(self.worker.run)

    def startCrawlingExtracter(self):
        for link in self.racesLinks:
            self.worker = UrlExtracterQThread(link,parent=self)
            self.worker.signals.finished.connect(self.loadRaceResults)
            self.threadpool.start(self.worker.run)

    def loadRacesLinks(self,data):
        self.racesLinks = data
        self.refreshCurrenWindow()

    def loadRaceResults(self,data):
        self.racesDone.append(data)
        self.refreshCurrenWindow()