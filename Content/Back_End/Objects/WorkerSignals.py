from typing import List
from PySide2.QtCore import QObject,Signal

class WorkerSignalsFinder(QObject):
    
    finished = Signal(list)


class WorkerSignalsExtracter(QObject):
    
    finished = Signal(list)
