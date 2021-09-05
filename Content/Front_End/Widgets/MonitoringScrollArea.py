
from Content.Front_End.Widgets.MonitoringQLabel import MonitoringQLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout, QListWidgetItem, QScrollArea, QScrollBar, QVBoxLayout, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class MonitoringScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super(MonitoringScrollArea,self).__init__(parent=parent)
        self.container = QGroupBox(self)
        self.containerLayout = QFormLayout()
        self.container.setLayout(self.containerLayout)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scrollBar = QScrollBar(self)

        self.setWidget(self.container)

        self.setVerticalScrollBar(self.scrollBar)


        for key,value in self.nativeParentWidget().racesDone.items():
            
            self.buttonLayout = QHBoxLayout()
            self.buttonLayout.addWidget(QPushButton("Yeet"))
            self.buttonLayout.addWidget(QPushButton("Yaat"))
            self.buttonLayout.addWidget(QPushButton("Yoot"))
            self.containerLayout.addRow(QLabel(key),self.buttonLayout)
