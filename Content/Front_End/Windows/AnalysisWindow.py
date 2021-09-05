from Content.Front_End.Widgets.MenuBar import MenuBar
from Content.Front_End.Widgets.SystemBar import SystemBar
from PyQt5.QtWidgets import QLineEdit, QWidget, QGridLayout, QGroupBox, QPushButton, QLabel

class AnalysisWindow(QWidget):

    # Window to watchover the crawled results
    def __init__(self,parent=None):
        super(AnalysisWindow,self).__init__(parent=parent)

        self.systemBar = SystemBar(parent=self)
        self.menuBar = MenuBar(parent=self)
        self.analysis = QGroupBox(self)
        self.analysisLayout = QGridLayout()
        self.analysis.setLayout(self.analysisLayout)
        self.analysis.setGeometry(180, 35, 1260, 660)
        
        self.analysis.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6)}")
        self.setStyleSheet("QLabel{color:white;background-color:rgba(0,0,0,0)} QPushButton{color:white;background-color:rgba(0,0,0,0)}")
        self.initUIContent()
        self.show()

    def initUIContent(self):

        self.searchBar = QLineEdit()
        self.analysisLayout.addWidget(self.searchBar)



        self.backButton = QPushButton("Courses")
        self.backButton.clicked.connect(
           lambda: self.nativeParentWidget().startDashboardWindow())
        self.analysisLayout.addWidget(self.backButton,6,6,1,1)