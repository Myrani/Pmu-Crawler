
from Content.Front_End.Windows.RaceDisplayWindow import RaceDisplayWindow
from Content.Front_End.Windows.AnalysisWindow import AnalysisWindow
from Content.Back_End.Objects.Scheduler import Scheduler
from Content.Back_End.Objects.DataHandler import DataHandler
from Content.Back_End.Crawlers.UrlExtracter import UrlExtracterQThread
from Content.Back_End.Crawlers.UrlFinder import UrlFinderQThread
from Content.Front_End.Windows.RacesWindow import RacesWindow
from Content.Front_End.Windows.DashboardWindow import DashboardWindow
from Content.Front_End.Windows.CrawlerWindow import CrawlerWindow
from Content.Front_End.Windows.MonitoringWindow import MonitoringWindow
from Content.Back_End.Objects.Worker import Worker
import os
import sys


from PySide2.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QLabel, QDesktopWidget
from PySide2.QtCore import QThreadPool, Qt, QPoint
from PySide2.QtGui import QPixmap



class MainWindow(QMainWindow):
    
    # First window generated, stocks all the long terms variable of the session between different windows
    
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(10, 10, 1280, 720)
            
        # Jobs handlers
        self.dataHandler = DataHandler(parent=self)     # Saving/loading data special object
          # Monitoring races special object

        # Durable variable initialization from save file
        self.racesFile = {}
        
        # Crawler cache variables
        self.racesLinks = []
        self.racesDone = {}

        
        # Monitoring cache variables

        self.pingList15minutes = []
        self.pingList30minutes = [] 
        self.pingList60minutes = []


        # Load data from save file
        self.dataHandler.loadFile()
        self.racesDone = self.dataHandler.getDayData()
        self.curratedRacesDone = self.dataHandler.generateRacesListFromDayData()



        # Window Opacity
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(0.95)
        self.setContentsMargins(0,0,0,0)
        #self.label_background.move(0, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:rgba(0, 0, 0, 1);")

        # Creation of the QThreadPool that will host Crawlers processes 
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(4)

        self.schedulerThreadpool = QThreadPool()
        self.schedulerThreadpool.setMaxThreadCount(4)



        #self.dataHandler.showCurrentData()
        #self.dataHandler.showSavedData()

        # Init futher main windows parametters
        self.init_Windows()

         # Start program with the Dashboard window first and show it
        self.startDashboardWindow()
    
    def init_Windows(self):

        # Last windows to that was shown, serves to refresh to show new data 
        self.lastWindow = ""

        # Quick Dynamic access dictionary to starWindows functions
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
    def print(self,x):
        print(x)

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

    def startRaceDisplayWindow(self,race):
        self.racesWindow = RaceDisplayWindow(race,parent=self)
        self.setCentralWidget(self.racesWindow)
        self.lastWindow = "raceDisplay"
        self.show()

    ### Refresh the last windows in case case of content update
    def refreshCurrenWindow(self):
        self.windowDict[self.lastWindow]()


    ### Bulk Web Crawling functions
    
    # Gets the current races lists
    def startCrawlingFinder(self):
        self.finder = UrlFinderQThread(parent=self)
        self.worker = Worker(self.finder.run)
        self.finder.signals.finished.connect(self.loadRacesLinks)
        self.threadpool.start(self.worker)

    # Gets all the races data
    def startCrawlingExtracter(self):
        for link in self.racesLinks:
            self.extracter = UrlExtracterQThread(link,parent=self)
            self.worker = Worker(self.extracter.run)
            
            self.extracter.signals.finished.connect(self.loadRaceResults)
            self.threadpool.start(self.worker)

    ### Precise url crawling functions


    def startPreciseRaceReExtraction(self,race):
        self.extracter = UrlExtracterQThread(race,parent=self)
        self.worker = Worker(self.extracter.run)
            
        self.extracter.signals.finished.connect(self.refreshRaceResults)
        self.threadpool.start(self.worker)




    def startRacesMonitoring(self):
        self.scheduler = Scheduler(parent=self) 




    def loadRacesLinks(self,data):
        self.racesLinks = data
        self.refreshCurrenWindow()

    def loadRaceResults(self,data):
        self.racesDone[data[0]] = data[1]
        if len(self.racesDone) == len(self.racesLinks):
            self.dataHandler.saveCurrentResults()
            self.dataHandler.showSavedData()
        self.curratedRacesDone = self.dataHandler.generateRacesListFromDayData()
        self.refreshCurrenWindow()


    def refreshRaceResults(self,data):
        self.racesDone[data[0]] = data[1]
        self.curratedRacesDone = self.dataHandler.generateRacesListFromDayData()
        self.refreshCurrenWindow()