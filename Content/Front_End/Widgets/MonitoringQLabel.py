from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtWidgets import QHBoxLayout, QListWidgetItem, QScrollArea, QVBoxLayout, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel



class MonitoringQLabel(QWidget):
    def __init__(self,message, parent = None):
        super(MonitoringQLabel,self).__init__(parent=parent)
        self.setStyleSheet("QWidget{background-color:rgba(255,255,255,0.6);} QLabel{background-color: rgba(255,255,255,0.5); color: black; } QPushButton{backgorund-color: rgba(0,0,255,1);}")
        self.message = message
        self.box = QGroupBox()
        self.box.setMinimumSize(100,300)
        self.layout = QHBoxLayout()
        self.box.setLayout(self.layout)

        self.initUI()
    
    def sizeHint(self):
        return QSize(500, 500)

    def initUI(self):    

        self.raceName = QLabel(self.message)
        self.button = QPushButton("Duh")
        self.button2 = QPushButton("Dah")

        self.layout.addWidget(self.raceName)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)




