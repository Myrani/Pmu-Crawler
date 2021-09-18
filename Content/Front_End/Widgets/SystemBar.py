from PySide2.QtWidgets import QGroupBox, QMainWindow, QWidget, QHBoxLayout, QPushButton
from PySide2.QtCore import QCoreApplication, QSize,Qt

class SystemBar(QWidget):
    def __init__(self, parent=None):
        super(SystemBar, self).__init__(parent=parent)
        self.systemBar = QGroupBox(self)
        self.systemBarLayout = QHBoxLayout()
        self.systemBar.setLayout(self.systemBarLayout)
        self.systemBar.setGeometry(180, -20, 1100, 75)
        self.systemBar.setContentsMargins(0,0,0,0)
        self.systemBar.setStyleSheet(
        " QGroupBox {background-color:rgba(0,0,0,0);border: solid 0px;}")



        self.windowGestionBar = QGroupBox(self)
        self.windowGestionBarLayout = QHBoxLayout()
        self.windowGestionBar.setLayout(self.windowGestionBarLayout)
        self.windowGestionBar.setGeometry(1175,-10,110,50)
        self.windowGestionBar.setStyleSheet(
        " QGroupBox {background-color:rgba(0,0,0,0);border: solid 0px;}")


        
        self.initUI()

    def initUI(self):

        self.minimizeButton = QPushButton("-")
        self.minimizeButton.setMinimumSize(QSize(50, 40))
        self.minimizeButton.setMaximumSize(QSize(50, 40))   
        self.minimizeButton.setStyleSheet(
        " QPushButton::hover{background-color: rgba(255, 255, 255, 0.2);color :black ;}; background-color:rgba(0,0,0,0.6); color: white;border : 0px;")
        self.minimizeButton.clicked.connect(
            lambda: QMainWindow.showMinimized(self.nativeParentWidget()))
        self.windowGestionBarLayout.addWidget(self.minimizeButton,0,Qt.AlignLeft)

        self.exitButton = QPushButton("X")
        self.exitButton.setMinimumSize(QSize(50, 40))
        self.exitButton.setMaximumSize(QSize(50, 40))
        self.exitButton.setStyleSheet(
        " QPushButton::hover{background-color: rgba(255, 0, 0, 0.95);color :black ;}; background-color:rgba(0,0,0,0.6); color: white;border : 0px;")
        self.exitButton.clicked.connect(
            lambda: QCoreApplication.exit())
        self.windowGestionBarLayout.addWidget(self.exitButton,-10,Qt.AlignLeft)