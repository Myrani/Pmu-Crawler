from PyQt5.QtWidgets import QGroupBox, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QCoreApplication, QSize,Qt

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
        self.mainWindow = self.parent().parent()
        self.functionDic = {"Accueil":self.mainWindow.startDashboardWindow,
                            "Récupération":self.mainWindow.startCrawlerWindow,
                            "Monitoring":self.mainWindow.startMonitoringWindow,
                            "Courses":self.mainWindow.startRacesWindow,
                            "X":self.mainWindow.startMonitoringWindow,
                            "Y":self.mainWindow.startCrawlerWindow}
        self.buttonList = []
        self.initUI()

    def initUI(self):
        for name,function in self.functionDic.items():
            self.buttonList.append(MenuBarButton(name,function,parent=self))
        for button in self.buttonList:
            self.menuBarLayout.addWidget(button.button,0,Qt.AlignTop)