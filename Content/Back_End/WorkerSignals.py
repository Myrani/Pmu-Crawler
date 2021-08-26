from typing import List
from PyQt5.QtCore import QObject,pyqtSignal

class WorkerSignalsFinder(QObject):
    
    finished = pyqtSignal(list)


class WorkerSignalsExtracter(QObject):
    
    finished = pyqtSignal(dict)
