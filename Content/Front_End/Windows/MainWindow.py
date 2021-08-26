from Content.Front_End.Windows.RacesWindow import RacesWindow
from Content.Front_End.Windows.DashboardWindow import DashboardWindow
from Content.Front_End.Windows.CrawlerWindow import CrawlerWindow
from Content.Front_End.Windows.MonitoringWindow import MonitoringWindow

import os
import sys


from PyQt5.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap



class MainWindow(QMainWindow):
    
    # First window generated, stocks all the long terms variable of the session between different windows
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(10, 10, 1280, 720)
        # Durable variable initialisation 
        self.racesFile = {}
        self.racesLinks = ["test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0","test","test0"]
        self.racesDone = []
        
        # Window Opacity
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowOpacity(0.95)
        self.setContentsMargins(0,0,0,0)
        #self.label_background.move(0, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:rgba(0, 0, 0, 1);")

        # Instanciation Window
        self.init_Windows()

        self.startDashboardWindow()
    
    def init_Windows(self):
        self.dashboardWindow = False
        self.monitoringWindow = False
        self.crawlerWindow = False
        self.racesWindow = False

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
   
    ### Dynamic window swapping ,call thoses functions to change the current displayed window
    def startDashboardWindow(self):

        self.dashboardWindow = DashboardWindow(parent=self)
        self.setCentralWidget(self.dashboardWindow)
        self.show()
   
    def startMonitoringWindow(self):

        self.monitoringWindow = MonitoringWindow(parent=self)
        self.setCentralWidget(self.monitoringWindow)
        self.show()
    
    def startCrawlerWindow(self):

        self.crawlerWindow = CrawlerWindow(parent=self)
        self.setCentralWidget(self.crawlerWindow)
        self.show()
    
    def startRacesWindow(self):

        self.racesWindow = RacesWindow(parent=self)
        self.setCentralWidget(self.racesWindow)
        self.show()


