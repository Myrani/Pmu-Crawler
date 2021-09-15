
from PyQt5.QtWidgets import QCheckBox, QGridLayout, QLabel, QWidget


class MonitoringCheckBox(QWidget):
    def __init__(self,key,parent=None):
        super(MonitoringCheckBox,self).__init__(parent=parent)
        self.parent = parent
        self.checkBoxLayout = QGridLayout()
            
        self.checkbox15 =  QCheckBox()
        self.checkbox30 =  QCheckBox()
        self.checkbox60 =  QCheckBox()

        self.boxesDict = {15:self.checkbox15,30:self.checkbox30,60:self.checkbox60}


        self.checkbox15.stateChanged.connect(lambda:self.onClick(self.checkbox15,key,15))
        self.checkbox30.stateChanged.connect(lambda:self.onClick(self.checkbox30,key,30))
        self.checkbox60.stateChanged.connect(lambda:self.onClick(self.checkbox60,key,60))


        self.label = QLabel(key)

        self.checkBoxLayout.addWidget(self.checkbox15,0,1,1,1)
        self.checkBoxLayout.addWidget(self.checkbox30,0,2,1,1)
        self.checkBoxLayout.addWidget(self.checkbox60,0,3,1,1)


        self.checkBoxLayout.addWidget(self.label,0,4,1,1)

        self.setLayout(self.checkBoxLayout)

    def onClick(self,button,key,time):
        if button.isChecked():
            if time == 15:
                self.nativeParentWidget().pingList15minutes.append(key)
            elif time == 30:
                self.nativeParentWidget().pingList30minutes.append(key)
            elif time == 60:
                self.nativeParentWidget().pingList60minutes.append(key)
        
        elif not button.isChecked() :
            if time == 15:
                self.nativeParentWidget().pingList15minutes.remove(key)
            elif time == 30:
                self.nativeParentWidget().pingList30minutes.remove(key)
            elif time == 60:
                self.nativeParentWidget().pingList60minutes.remove(key)


        #print(self.nativeParentWidget().pingList15minutes)
        #print(self.nativeParentWidget().pingList30minutes)
        #print(self.nativeParentWidget().pingList60minutes)
  
            