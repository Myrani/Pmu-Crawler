from Content.Front_End.Widgets.RaceContestantLabel import RaceContestantLabel
from Content.Front_End.Widgets.RacesToolTip import RacesToolTip
from Content.Front_End.Widgets.RacesScrollArea import RacesScrollArea
from Content.Front_End.Widgets.MenuBar import MenuBar
from Content.Front_End.Widgets.SystemBar import SystemBar
from PySide2.QtWidgets import QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class RaceDisplayWindow(QWidget):

    # Window to watchover the crawled results
    def __init__(self,race,parent=None):
        super(RaceDisplayWindow,self).__init__(parent=parent)

        self.name = race.getName()
        self.data = race.getRawData()

        
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
        for key,result in self.data.items():
            object = RaceContestantLabel(result)
            self.racesScrollArea.containerLayout.addWidget(object,i,0,1,1)
            i +=1
        # print(self.racesScrollArea.container.children())

        self.backButton = QPushButton("Courses")
        self.backButton.clicked.connect(
           lambda: self.nativeParentWidget().startRaceDisplayWindow(self.name,self.data))
        self.racesMenuLayout.addWidget(self.backButton,0,11,1,1)