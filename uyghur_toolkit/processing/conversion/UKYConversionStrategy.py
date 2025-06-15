# -*- coding: utf-8 -*-
"""
UKY转换策略实现模块
提供维吾尔语UKY转写方案的转换处理器集合和策略实现。
"""
from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.UKYProcessors import *

defaultUKYContainer = (ProcessorContainer(ProcesClass.UKY)
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
    """UKY转换策略实现类

    继承自ConversionStrategy，使用预定义的UKY处理器容器
    实现维吾尔语UKY转写方案的转换功能。
    """
    def __init__(self):
        super().__init__(ProcesClass.UKY, defaultUKYContainer)
