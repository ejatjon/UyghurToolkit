# -*- coding: utf-8 -*-
"""处理器抽象基类模块
该模块定义了处理器的抽象基类，为具体处理器实现提供统一接口和基础功能。
任何处理逻辑需要实现Processor（处理器）类，
ProcesType 处理器属性，如 NORMALIZATION | REVERSE 表示处理恢复标准化的字符（标准化的反操作）
ProcesType 通过组合 REVERSE 表示反向操作
"""
import abc

from uyghur_toolkit.processing.ProcesClass import ProcesClass


class Processor(abc.ABC):
    """
    处理器抽象基类，为具体处理器提供统一接口
    职责：
    1. 定义处理器的标准调用接口
    2. 封装处理器的基础属性和方法

    参数：
    p_class: 处理器所属分类（ProcesClass枚举）
    p_type: 处理器类型标识符
    name:   处理器名称

    关键方法：
    process(): 抽象方法，需在子类实现具体处理逻辑
    """
    def __init__(self, p_class: ProcesClass, p_type: int, name: str):
        self.__proces_class = p_class
        self.__proces_type = p_type
        self.__name = name

    @abc.abstractmethod
    def process(self, *args, **kwargs):
        """
        执行处理操作，需在子类实现具体逻辑

        参数：
        *args:   可变位置参数
        **kwargs: 可变关键字参数

        返回：
        处理结果（由子类实现决定）
        """
        pass

    def getName(self) -> str:
        """
        返回处理器名
        :return: 处理器名
        """
        return self.__name

    def getProcesClass(self) -> ProcesClass:
        """
        返回处理器所属分类
        :return: 处理器所属分类
        """
        return self.__proces_class

    def getProcesType(self) -> int:
        """
        返回处理器类型标识符
        :return: 处理器类型标识符
        """
        return self.__proces_type
