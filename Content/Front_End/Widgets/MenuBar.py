from PySide2.QtWidgets import QGroupBox, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PySide2.QtCore import QCoreApplication, QSize,Qt
from PySide2 import QtGui

from Content.Front_End.Widgets.MenuBarButton import MenuBarButton

class MenuBar(QWidget):
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent=parent)

        self.menuBar = QGroupBox(self)
        self.menuBarLayout = QVBoxLayout(self)
        self.menuBar.setLayout(self.menuBarLayout)
        self.menuBar.setGeometry(-10, -10, 200, 600)
        self.menuBar.setContentsMargins(-1,-1,-1,-1)
        self.menuBar.setStyleSheet(
        " QGroupBox {background-color:rgba(0,0,0,0.6);border: solid 0px;}")
        
        # Fix nativeParentWidget not working
        self.mainWindow = self.parent().parent()
        self.functionDic = {"Accueil":self.mainWindow.startDashboardWindow,
                            "Récupération":self.mainWindow.startCrawlerWindow,
                            "Surveillance":self.mainWindow.startMonitoringWindow,
                            "Courses":self.mainWindow.startRacesWindow,
                            "Analyse":self.mainWindow.startAnalysisWindow,
                            "Y":self.mainWindow.startCrawlerWindow}
        self.buttonList = []
        self.initUI()

    def initUI(self):
        for name,function in self.functionDic.items():
            self.buttonList.append(MenuBarButton(name,function,parent=self))
        for button in self.buttonList:
            self.menuBarLayout.addWidget(button.button,0,Qt.AlignTop)