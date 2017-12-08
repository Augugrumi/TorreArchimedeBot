from abc import ABCMeta, abstractmethod

class AbsHandler:
    __metaclass__ = ABCMeta

    @abstractmethod
    def handleMessage(self): pass
