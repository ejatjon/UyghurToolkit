from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.ULYProcessors import *

defaultULYContainer=(ProcessorContainer(ProcesClass.UYY)
                     .register(ULYNumberProcessor())
                     .register(ULYNumberReverseProcessor())
                     .register(ULYDateProcessor())
                     .register(ULYDateAndNumberReverseProcessor())
                     .register(ULYSymbolsProcessor())
                     .register(ULYSymbolsReverseProcessor())
                     .register(ULYNormalizeProcessor())
                     .register(ULYNormalizeReverseProcessor())
                     .register(ULYToIPAProcessor())
                     .register(ULYToUYYProcessor())
                     .register(ULYToUKYProcessor())
                     .register(ULYToUEYProcessor())
                     .register(ULYDivideSyllablesProcessor())
                     )


class ULYConversionStrategy(ConversionStrategy):
    def __init__(self):
        super().__init__(ProcesClass.ULY,defaultULYContainer)
