from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.UYYProcessors import *

defaultUYYContainer=(ProcessorContainer(ProcesClass.UYY)
                     .register(UYYNumberProcessor())
                     .register(UYYNumberReverseProcessor())
                     .register(UYYDateProcessor())
                     .register(UYYDateAndNumberReverseProcessor())
                     .register(UYYSymbolsProcessor())
                     .register(UYYSymbolsReverseProcessor())
                     .register(UYYNormalizeProcessor())
                     .register(UYYNormalizeReverseProcessor())
                     .register(UYYToIPAProcessor())
                     .register(UYYToULYProcessor())
                     .register(UYYToUKYProcessor())
                     .register(UYYToUEYProcessor())
                     .register(UYYDivideSyllablesProcessor())
                     )


class UYYConversionStrategy(ConversionStrategy):
    def __init__(self):
        super().__init__(ProcesClass.UYY,defaultUYYContainer)
