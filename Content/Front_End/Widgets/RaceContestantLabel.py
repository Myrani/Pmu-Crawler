from PySide2.QtCore import QRect, QSize, Qt
from PySide2.QtWidgets import QHBoxLayout, QListWidgetItem, QScrollArea, QVBoxLayout, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel



class RaceContestantLabel(QWidget):
    def __init__(self,contestantInfo, parent = None):
        super(RaceContestantLabel,self).__init__(parent=parent)
        self.contestantInfo = contestantInfo

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.setMinimumSize(50,50)

        self.initUI()
    
    def sizeHint(self):
        return QSize(100, 500)

    def initUI(self):    

        for element in self.contestantInfo:
            self.object = QLabel(element,parent=self)
            self.object.setAlignment(Qt.AlignCenter)
            self.object.setStyleSheet("background-color: rgba(0,0,0,0.5); color: white; ")
            self.layout.addWidget(self.object)

