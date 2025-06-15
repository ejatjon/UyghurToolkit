# -*- coding: utf-8 -*-
"""
ProcessorContainer 模块：管理处理器（Processor）的注册、注销和查询的抽象容器类
"""

from abc import ABC
from typing import Union

from uyghur_toolkit import LOG
from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.processor.Processor import Processor


class ProcessorContainer(ABC):
    """
    处理器容器抽象基类，用于管理特定处理类别（ProcesClass）下的处理器集合

    功能：
    - 注册/注销处理器
    - 查询已注册处理器信息
    - 按类型获取处理器实例
    """

    def __init__(self, t: ProcesClass):
        self.__t = t
        self.__processors: dict[int, Processor] = {}

    def register(self, p: Processor):
        """
        注册处理器
        :param p: 处理器实例
        :return: 返回类本身
        """
        if p.getProcesClass() != self.__t:
            LOG.ERROR("Invalid Processor Class.")
            return self
        if p.getProcesType() in self.__processors:
            LOG.WARNING(
                f"Processor({p.getName()}) already registered or conflicts with existing processors.\nView the "
                f"existing processor via getProcessorsInfo")
            return self
        else:
            self.__processors[p.getProcesType()] = p
            LOG.INFO(f"Processor({p.getName()}) registered.")
        return self

    def unregister(self, p: Processor):
        """
        注销处理器
        :param p: 处理器实例
        :return: 返回类本身
        """
        if p.getProcesType() in self.__processors and self.__processors[p.getProcesType()].getName() == p.getName():
            del self.__processors[p.getProcesType()]
            LOG.INFO(f"Processor({p.getName()}) unregistered.")
        else:
            LOG.WARNING(f"Processor({p.getName()}) not registered.")
        return self

    def getProcessorsInfo(self):
        """
        获取已注册处理器信息
        :return: 返回处理器信息列表
        """
        return [(p.getName(), p.getProcesType(), p.getProcesClass()) for p in self.__processors.values()]

    # Python 3.10 以下版本不支持 X | Y 联合类型注解语法。使用 typing.Union 替代 | 操作符进行类型注解，跟Processor | None 没有区别
    def getProcessor(self, p_type: Union[ProcesType, int]) -> Union[Processor, None]:
        """
        按类型获取处理器实例
        :param p_type: 处理器类型
        :return: 处理器实例
        """
        return self.__processors.get(p_type, None)
