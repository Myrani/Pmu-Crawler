
import os
import sys


from PyQt5.QtWidgets import QMainWindow, QGraphicsOpacityEffect, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap

from Content.Front_End.Windows.DashboardWindow import DashboardWindow

class MainWindow(QMainWindow):
    
    # First window generated, stocks all the long terms variable of the session between different windows
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(10, 10, 1280, 720)

        # Window Opacity
        self.opacity_effect = QGraphicsOpacityEffect()
        self.setWindowOpacity(0.95)
        self.setContentsMargins(0,0,0,0)
        #self.label_background.move(0, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setStyleSheet("background-color:#6d3a91;")

        self.startDashboardWindow()

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
    
    ### Dynamic window swapping ,call thoses functions to change the current displayed window
    def startDashboardWindow(self):
        self.dashboardWindow = DashboardWindow(parent=self)
        self.setCentralWidget(self.dashboardWindow)
        self.show()

