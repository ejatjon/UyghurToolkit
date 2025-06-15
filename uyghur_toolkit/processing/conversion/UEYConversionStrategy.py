# -*- coding: utf-8 -*-
"""
维吾尔语(UEY)转换策略模块
包含UEYConversionStrategy类及默认处理器容器配置
实现维吾尔语文本的多种转换处理策略
"""

from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.UEYProcessors import *

defaultUEYContainer = (ProcessorContainer(ProcesClass.UEY)
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
    """维吾尔语(UEY)转换策略实现类
       继承ConversionStrategy基类，使用预定义的默认处理器容器
       提供维吾尔语文本的多种转换处理能力
       """

    def __init__(self):
        super().__init__(ProcesClass.UEY, defaultUEYContainer)
