from Content.Front_End.Widgets.MenuBar import MenuBar
from Content.Front_End.Widgets.SystemBar import SystemBar
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QPushButton, QLabel


class DashboardWindow(QWidget):

    # Window generated by a SystemBar to help the user
    def __init__(self,parent=None):
        super(DashboardWindow,self).__init__(parent=parent)

        self.systemBar = SystemBar(self)
        self.menuBar = MenuBar(self)
        self.monitoringMenu = QGroupBox(self)
        self.monitoringMenuLayout = QGridLayout()
        self.monitoringMenu.setLayout(self.monitoringMenuLayout)
        self.monitoringMenu.setGeometry(200, 40, 1260, 660)
        
        self.monitoringMenu.setStyleSheet(
            "QGroupBox {border:3px solid black;background-color:rgba(0,0,0,0.6)}")

        self.initUIContent()
        self.show()

    def initUIContent(self):

        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(
            lambda: self.nativeParentWidget().startDashboardWindow())
        self.monitoringMenuLayout.addWidget(self.backButton,6,6,1,1)