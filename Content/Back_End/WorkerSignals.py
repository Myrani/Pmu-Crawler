from typing import List
from PyQt5.QtCore import QObject,pyqtSignal

class WorkerSignals(QObject):
    
    finished = pyqtSignal(list)

