from PyQt5.QtWidgets import QGroupBox, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QCoreApplication, QSize,Qt

from Content.Front_End.Widgets.MenuBarButton import MenuBarButton

class MenuBar(QWidget):
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent=parent)
        self.menuBar = QGroupBox(self)
        self.menuBarLayout = QVBoxLayout(self)
        self.menuBar.setLayout(self.menuBarLayout)
        self.menuBar.setGeometry(-10, 35, 200, 500)
        self.menuBar.setContentsMargins(-1,-1,-1,-1)
        self.menuBar.setStyleSheet(
        " QGroupBox {background-color:rgba(0,0,0,0.6);border: solid 0px;}")
        
        self.buttonList = []
        self.initUI()

    def initUI(self):
    
        for i in range(0,5):
            self.buttonList.append(MenuBarButton(self))
        for button in self.buttonList:
            self.menuBarLayout.addWidget(button.button,0,Qt.AlignTop)