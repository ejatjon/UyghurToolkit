from abc import ABC

from uyghur_toolkit import LOG
from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.processor.Processor import Processor


class ProcessorContainer(ABC):
    def __init__(self, t: ProcesClass):
        self.__t = t
        self.__processors: dict[int, Processor] = {}

    def register(self, p: Processor):
        if p.getProcesClass() != self.__t:
            LOG.ERROR("Invalid Processor Class.")
            return self
        if p.getProcesType() in self.__processors:
            LOG.WARNING(
                f"Processor({p.getName()}) already registered or conflicts with existing processors.\nView the existing processor via getProcessorsInfo")
            return self
        else:
            self.__processors[p.getProcesType()] = p
            LOG.INFO(f"Processor({p.getName()}) registered.")
        return self

    def unregister(self, p: Processor):
        if p.getProcesType() in self.__processors and self.__processors[p.getProcesType()].getName() == p.getName():
            del self.__processors[p.getProcesType()]
            LOG.INFO(f"Processor({p.getName()}) unregistered.")
        else:
            LOG.WARNING(f"Processor({p.getName()}) not registered.")
        return self

    def getProcessorsInfo(self):
        return [(p.getName(), p.getProcesType(), p.getProcesClass()) for p in self.__processors.values()]

    def getProcessor(self, p_type: ProcesType | int) -> Processor | None:
        return self.__processors.get(p_type, None)


