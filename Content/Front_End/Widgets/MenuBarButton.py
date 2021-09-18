from PySide2 import QtWidgets
from PySide2.QtWidgets import QGroupBox, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PySide2.QtCore import QCoreApplication, QEvent, QSize,Qt

class MenuBarButton(QWidget):
    def __init__(self,name,function, parent=None):
        super(MenuBarButton, self).__init__(parent=parent)
        self.button = QPushButton(str(name))
        self.function = function
        self.button.setMinimumSize(QSize(200, 100))
        self.button.setMaximumSize(QSize(200, 100))
        self.button.setStyleSheet(
        " QPushButton::hover{background-color: rgba(255, 255, 255, 0.6);color :black ;}; background-color:rgba(0,0,0,0.6); color: white;border : 0px;")
        self.initUI()
        self.button.installEventFilter(self)
    
    def initUI(self):
        self.button.clicked.connect(lambda:self.function())


    def eventFilter(self, source, event):
        if event.type() == QEvent.HoverEnter:
            pass
            #self.function()
            #self.button.setStyleSheet("QPushButton{background-color: rgba(255, 255, 255, 0.6);color :black ;}")
        
        elif event.type() == QEvent.HoverLeave:

            pass
        return super().eventFilter(source, event)


    