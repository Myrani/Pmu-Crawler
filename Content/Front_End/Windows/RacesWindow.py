from Content.Front_End.Widgets.MenuBar import MenuBar
from Content.Front_End.Widgets.SystemBar import SystemBar
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class RacesWindow(QWidget):

    # Window to watchover the crawled results
    def __init__(self,parent=None):
        super(RacesWindow,self).__init__(parent=parent)

        self.systemBar = SystemBar(parent=self)
        self.menuBar = MenuBar(parent=self)
        self.monitoringMenu = QGroupBox(self)
        self.monitoringMenuLayout = QGridLayout()
        self.monitoringMenu.setLayout(self.monitoringMenuLayout)
        self.monitoringMenu.setGeometry(180, 35, 1260, 660)
        
        self.monitoringMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6)}")
        self.setStyleSheet("QLabel{color:white;background-color:rgba(0,0,0,0)} QPushButton{color:white;background-color:rgba(0,0,0,0)}")
        self.initUIContent()
        self.show()

    def initUIContent(self):
        self.backButton = QPushButton("Courses")
        self.backButton.clicked.connect(
           lambda: self.nativeParentWidget().startDashboardWindow())
        self.monitoringMenuLayout.addWidget(self.backButton,6,6,1,1)