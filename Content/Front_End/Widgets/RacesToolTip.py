from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QCheckBox, QFormLayout, QHBoxLayout, QListWidgetItem, QScrollArea, QScrollBar, QVBoxLayout, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class RacesToolTip(QWidget):
    def __init__(self, name,data,parent=None):
        super(RacesToolTip,self).__init__(parent=parent)
        self.name = name
        self.data = data

        self.container = QGroupBox(parent=self)
        self.containerLayout = QHBoxLayout()
        self.container.setLayout(self.containerLayout)

        self.setMinimumSize(100,100)
        self.button = QPushButton(self.name,parent=self)
        self.button.clicked.connect(lambda:self.nativeParentWidget().startRaceDisplayWindow(self.name,self.data))
        self.containerLayout.addWidget(self.button)

        self.setStyleSheet("QPushButton{color : white;background-color:black;border: solid 2px white;}")
        