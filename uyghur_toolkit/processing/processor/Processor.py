import enum
from abc import ABC, abstractmethod

from uyghur_toolkit.processing.ProcesClass import ProcesClass


class Processor(ABC):
    def __init__(self, p_class: ProcesClass, p_type: int, name: str):
        self.__proces_class = p_class
        self.__proces_type = p_type
        self.__name=name

    def __call__(self, *args, **kwargs):
        return self.process(*args, **kwargs)

    @abstractmethod
    def process(self,*args, **kwargs):
        pass

    def getName(self):
        return self.__name

    def getProcesClass(self):
        return self.__proces_class

    def getProcesType(self):
        return self.__proces_type
