from Content.Front_End.Windows.RaceDisplayWindow import RaceDisplayWindow
from Content.Front_End.Windows.AnalysisWindow import AnalysisWindow
from Content.Back_End.Widgets.Scheduler import Scheduler
from Content.Back_End.Widgets.DataHandler import DataHandler
from Content.Back_End.Crawlers.UrlExtracter import UrlExtracterQThread
from Content.Back_End.Crawlers.UrlFinder import UrlFinderQThread
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
        
        # Jobs handlers
        self.dataHandler = DataHandler(parent=self)
        self.scheduleHandler = Scheduler(parent=self)

        # Durable variable initialisation 
        self.racesFile = {}
        
        # Crawler 
        self.racesLinks = []
        self.racesDone = {}
        
        # Monitoring

        self.pingList15minutes = []
        self.pingList30minutes = [] 
        self.pingList60minutes = []


        # Load la save 

        self.dataHandler.loadFile()
        self.racesDone = self.dataHandler.getDayData()

        # Window Opacity
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(0.95)
        self.setContentsMargins(0,0,0,0)
        #self.label_background.move(0, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:rgba(0, 0, 0, 1);")

        # Création de la Thread Pool 
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(4)

        #self.dataHandler.showCurrentData()
        #self.dataHandler.showSavedData()

        # Instanciation de l'acceuil
        self.init_Windows()

        self.startDashboardWindow()
    
    def init_Windows(self):
        self.dashboardWindow = False
        self.monitoringWindow = False
        self.crawlerWindow = False
        self.racesWindow = False

        self.lastWindow = ""

        self.windowDict = { "dashboard":self.startDashboardWindow,
                            "crawler":self.startCrawlerWindow,
                            "monitoring":self.startMonitoringWindow,
                            "races":self.startRacesWindow,
                            "analysis":self.startAnalysisWindow,
                            "raceDisplay":self.startRaceDisplayWindow}

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

    def startAnalysisWindow(self):
        self.analysisWindow = AnalysisWindow(parent=self)
        self.setCentralWidget(self.analysisWindow)
        self.lastWindow = "analysis"
        self.show()

    def startRaceDisplayWindow(self,name,data):
        self.racesWindow = RaceDisplayWindow(name,data,parent=self)
        self.setCentralWidget(self.racesWindow)
        self.lastWindow = "raceDisplay"
        self.show()

    ### Refresh the last windows in case case of content update
    def refreshCurrenWindow(self):
        self.windowDict[self.lastWindow]()


    ### Bulk Web Crawling functions
    
    # Gets the current races lists
    def startCrawlingFinder(self):
        self.worker = UrlFinderQThread(parent=self)
        self.worker.signals.finished.connect(self.loadRacesLinks)
        self.threadpool.start(self.worker.run)

    # Gets all the races data
    def startCrawlingExtracter(self):
        for link in self.racesLinks:
            self.worker = UrlExtracterQThread(link,parent=self)
            self.worker.signals.finished.connect(self.loadRaceResults)
            self.threadpool.start(self.worker.run)

    ### Precise url crawling functions

    def startPreciseExtraction(self,raceUrl):
       # self.worker = UrlFinderQThread(parent=self)
       # self.worker.signals.finished.connect(self.loadRacesLinks)
       # self.threadpool.start(self.worker.run)
        pass


    def loadRacesLinks(self,data):
        self.racesLinks = data
        self.refreshCurrenWindow()

    def loadRaceResults(self,data):
        self.racesDone[data[0]] = data[1]
        if len(self.racesDone) == len(self.racesLinks):
            self.dataHandler.saveCurrentResults()
            self.dataHandler.showSavedData()
        self.refreshCurrenWindow()