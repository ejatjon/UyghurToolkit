# -*- coding: utf-8 -*-
"""
提供文本转换策略的抽象基类实现，用于管理多步骤转换流水线
"""
from abc import ABC
from typing import Union

from uyghur_toolkit import LOG
from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.conversion.ProcessorContainer import ProcessorContainer


class ConversionStrategy(ABC):
    """
    转换策略抽象基类
    职责：
    1. 管理处理选项流水线
    2. 通过处理器容器执行具体转换逻辑
    """

    def __init__(self, p_class: ProcesClass, p_container: ProcessorContainer):
        self.__p_class = p_class
        self.__p_container: ProcessorContainer = p_container
        self.options: list[int] = []

    def get_strategy_type(self) -> ProcesClass:
        """
        获取转换策略类型（UEY,ULT,UKY,UYY,IPA）
        :return: 转换策略类型
        """
        return self.__p_class

    def add_convertion_option(self, option: Union[ProcesType, int]) -> 'ConversionStrategy':
        """
        添加转换选项
        :param option: 转换选项
        :return: 类本身
        """
        if not self.__p_container.getProcessor(option):
            LOG.ERROR("Invalid option")
            return self
        self.options.append(option)
        LOG.DEBUG("ProcesType added")
        return self

    def clear_convertion_options(self) -> 'ConversionStrategy':
        """
        清除转换选项
        :return: 类本身
        """
        self.options = []
        LOG.DEBUG("ProcesType removed")
        return self

    def convert(self, text: str) -> str:
        """
        执行转换逻辑
        :param text: 待转换文本
        :return: 转换结果
        """
        for option in self.options:
            processor = self.__p_container.getProcessor(option)
            if processor is None:
                LOG.ERROR(f"Invalid option {option}!")
                return text
            text = processor.process(text)
        return text
