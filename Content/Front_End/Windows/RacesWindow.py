from Content.Front_End.Widgets.RacesToolTip import RacesToolTip
from Content.Front_End.Widgets.RacesScrollArea import RacesScrollArea
from Content.Front_End.Widgets.MenuBar import MenuBar
from Content.Front_End.Widgets.SystemBar import SystemBar
from PySide2.QtWidgets import QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class RacesWindow(QWidget):

    # Window to watchover the crawled results
    def __init__(self,parent=None):
        super(RacesWindow,self).__init__(parent=parent)

        self.systemBar = SystemBar(parent=self)
        self.menuBar = MenuBar(parent=self)
        self.racesMenu = QGroupBox(self)
        self.racesMenuLayout = QGridLayout()
        self.racesMenu.setLayout(self.racesMenuLayout)
        self.racesMenu.setGeometry(180, 35, 1260, 660)
        
        self.racesMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6)}")
        self.setStyleSheet("QLabel{color:white;background-color:rgba(0,0,0,0)} QPushButton{color:white;background-color:rgba(0,0,0,0)}")
        self.initUIContent()
        self.show()

    def initUIContent(self):

        self.racesScrollArea = RacesScrollArea(parent=self)
        self.racesMenuLayout.addWidget(self.racesScrollArea,0,0,5,7)

        i = 0
        d = 0
        for course in self.nativeParentWidget().curratedRacesDone:
            object = RacesToolTip(course,parent=self)
            self.racesScrollArea.containerLayout.addWidget(object,d,i,1,1)
            if i == 3:
                d+=1
                i=-1
            i+=1


        self.backButton = QPushButton("Courses")
        self.backButton.clicked.connect(
           lambda: self.nativeParentWidget().startDashboardWindow())
        self.racesMenuLayout.addWidget(self.backButton,0,11,1,1)