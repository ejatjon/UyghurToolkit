from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.UKYProcessors import *

defaultUKYContainer=(ProcessorContainer(ProcesClass.UKY)
                     .register(UKYNumberProcessor())
                     .register(UKYNumberReverseProcessor())
                     .register(UKYDateProcessor())
                     .register(UKYDateAndNumberReverseProcessor())
                     .register(UKYSymbolsProcessor())
                     .register(UKYSymbolsReverseProcessor())
                     .register(UKYNormalizeProcessor())
                     .register(UKYNormalizeReverseProcessor())
                     .register(UKYToIPAProcessor())
                     .register(UKYToUYYProcessor())
                     .register(UKYToULYProcessor())
                     .register(UKYToUEYProcessor())
                     .register(UKYDivideSyllablesProcessor())
                     )


class UKYConversionStrategy(ConversionStrategy):
    def __init__(self):
        super().__init__(ProcesClass.UKY,defaultUKYContainer)
