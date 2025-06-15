# -*- coding: utf-8 -*-
"""
该模块实现了ULY（维吾尔语拉丁字母）的转换策略，
包含默认的处理器容器配置和转换策略类定义。
"""
from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.ULYProcessors import *

defaultULYContainer = (ProcessorContainer(ProcesClass.UYY)
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
    """
    该类实现了ULY（维吾尔语拉丁字母）的转换策略，
    继承自ConversionStrategy类。
    """
    def __init__(self):
        super().__init__(ProcesClass.ULY, defaultULYContainer)
