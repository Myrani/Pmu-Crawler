from Content.Back_End.Objects.Race import Race
from PySide2.QtCore import QObject,Signal

class WorkerSignalsFinder(QObject):
    
    finished = Signal(list)


class WorkerSignalsExtracter(QObject):
    
    finished = Signal(list)


class SchedulerSignals(QObject):
    
    ping = Signal(Race)
    extracted = Signal(dict)