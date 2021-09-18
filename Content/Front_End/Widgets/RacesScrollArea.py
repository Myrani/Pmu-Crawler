from PySide2.QtCore import QRect, Qt
from PySide2.QtWidgets import QCheckBox, QFormLayout, QHBoxLayout, QListWidgetItem, QScrollArea, QScrollBar, QVBoxLayout, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class RacesScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super(RacesScrollArea,self).__init__(parent=parent)
        self.container = QGroupBox(self)
        self.containerLayout = QGridLayout()
        self.container.setLayout(self.containerLayout)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scrollBar = QScrollBar(self)

        self.setWidget(self.container)

        self.setVerticalScrollBar(self.scrollBar)
