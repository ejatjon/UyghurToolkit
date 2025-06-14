from abc import ABC

from uyghur_toolkit import LOG
from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer


class ConversionStrategy(ABC):
    """
    ConversionStrategy（转换策略）
    每个转换策略需要提供自己的ProcessorContainer
    """
    def __init__(self,p_class:ProcesClass,p_container:ProcessorContainer):
        self.__p_class=p_class
        self.__p_container:ProcessorContainer=p_container
        self.options:list[int]=[]

    def getConvertType(self):
        return self.__p_class

    def addConvertionOption(self, option: ProcesType | int):
        if not self.__p_container.getProcessor(option):
            LOG.ERROR("Invalid option")
            return self
        self.options.append(option)
        LOG.DEBUG("ProcesType added")
        return self

    def clearConvertionOptions(self):
        self.options = []
        LOG.DEBUG("ProcesType removed")

    def convert(self, text: str) -> str:
        for option in self.options:
            processor = self.__p_container.getProcessor(option)
            if processor is None:
                LOG.ERROR(f"Invalid option {option}!")
                return text
            text = processor.process(text)
        return  text

    def __call__(self, text: str) -> str:
        return self.convert(text)

