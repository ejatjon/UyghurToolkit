from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.UEYProcessors import *

defaultUEYContainer=(ProcessorContainer(ProcesClass.UEY)
                     .register(UEYNumberProcessor())
                     .register(UEYNumberReverseProcessor())
                     .register(UEYDateProcessor())
                     .register(UEYDateAndNumberReverseProcessor())
                     .register(UEYSymbolsProcessor())
                     .register(UEYSymbolsReverseProcessor())
                     .register(UEYNormalizeProcessor())
                     .register(UEYNormalizeReverseProcessor())
                     .register(UEYToIPAProcessor())
                     .register(UEYToUYYProcessor())
                     .register(UEYToULYProcessor())
                     .register(UEYToUKYProcessor())
                     .register(UEYDivideSyllablesProcessor())
                     )


class UEYConversionStrategy(ConversionStrategy):
    def __init__(self):
        super().__init__(ProcesClass.UEY,defaultUEYContainer)
