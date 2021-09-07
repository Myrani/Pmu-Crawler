
from Content.Front_End.Widgets.MonitoringQLabel import MonitoringQLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QCheckBox, QFormLayout, QHBoxLayout, QListWidgetItem, QScrollArea, QScrollBar, QVBoxLayout, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class MonitoringScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super(MonitoringScrollArea,self).__init__(parent=parent)
        self.container = QGroupBox(self)
        self.containerLayout = QGridLayout()
        self.container.setLayout(self.containerLayout)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scrollBar = QScrollBar(self)

        self.setWidget(self.container)

        self.setVerticalScrollBar(self.scrollBar)





