from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.IPAProcessors import *

defaultIPAContainer=(ProcessorContainer(ProcesClass.IPA)
                     .register(IPANumberProcessor())
                     .register(IPANumberReverseProcessor())
                     .register(IPADateProcessor())
                     .register(IPADateAndNumberReverseProcessor())
                     .register(IPASymbolsProcessor())
                     .register(IPASymbolsReverseProcessor())
                     .register(IPANormalizeProcessor())
                     .register(IPANormalizeReverseProcessor())
                     .register(IPAToUEYProcessor())
                     .register(IPAToUYYProcessor())
                     .register(IPAToULYProcessor())
                     .register(IPAToUKYProcessor())
                     .register(IPADivideSyllablesProcessor())
                     )


class IPAConversionStrategy(ConversionStrategy):
    def __init__(self):
        super().__init__(ProcesClass.IPA,defaultIPAContainer)
