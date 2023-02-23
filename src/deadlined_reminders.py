from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil import parser
from datetime import datetime

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
    
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True
    
class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parser.parse(timestr=date, dayfirst=True)
        self.text = text

    def is_due(self):
        return self.date <= datetime.now()
    
    def __iter__(self):
        formatted_date = self.date.isoformat()
        return iter([self.text, formatted_date])