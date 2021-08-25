from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QCoreApplication, QSize,Qt

class MenuBarButton(QWidget):
    def __init__(self, parent=None):
        super(MenuBarButton, self).__init__(parent=parent)
        self.button = QPushButton("Button")
        self.button.setMinimumSize(QSize(200, 100))
        self.button.setMaximumSize(QSize(200, 100))
        self.button.setStyleSheet(
        " QPushButton::hover{background-color: rgba(255, 255, 255, 0.6);color :black ;}; background-color:rgba(0,0,0,0.6); color: white;border : 0px;")
        self.initUI()
    def initUI(self):
        pass