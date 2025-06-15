# -*- coding: utf-8 -*-
"""
该模块实现了国际音标(IPA)的转换策略，包含默认的IPA处理器容器和转换策略类。
提供数字、日期、符号的IPA转换及标准化处理，支持多种拉丁转写方案(UEY/UYY/ULY/UKY)的音节划分。
"""
from uyghur_toolkit.processing.conversion.ConversionStrategy import ConversionStrategy
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer
from uyghur_toolkit.processing.processor.default.IPAProcessors import *

defaultIPAContainer = (ProcessorContainer(ProcesClass.IPA)
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
    """
    国际音标(IPA)的转换策略类
    """
    def __init__(self):
        super().__init__(ProcesClass.IPA, defaultIPAContainer)
