from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil import parser

class DeadlinedMetaReminder(Iterable):
    def __init__(self, metaclass=ABCMeta):
        self.metaclass = metaclass
    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass
    
class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parser.parse(timestr=date, dayfirst=True)
        self.text = text
