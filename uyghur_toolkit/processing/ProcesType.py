# -*- coding: utf-8 -*-
"""定义文本处理类型的枚举类，用于表示不同的维吾尔语文本处理操作类型"""
import enum
from uyghur_toolkit.utils.other import BIT


class ProcesType(enum.IntEnum):
    """文本处理操作类型枚举

   使用位运算组合多个处理类型（如: NORMALIZATION | REVERSE）
   每个枚举值代表不同的文本处理操作
   """
    UNDEFINED = 0           #: 未定义操作
    NORMALIZATION = BIT(0)  #: 文本标准化处理（统一字符形式）
    NUMBER = BIT(1)         #: 数字格式转换（阿拉伯数字↔维文数字）
    SYMBOL = BIT(2)         #: 符号格式转换（标点/货币符号等）
    DATE = BIT(3)           #: 日期格式转换（数字公历↔维文日期）
    TO_UEY = BIT(4)         #: 转换为老维文（UEY）
    TO_UKY = BIT(5)         #: 转换为西里尔维文（UKY）
    TO_ULY = BIT(6)         #: 转换为拉丁维文（ULY）
    TO_UYY = BIT(7)         #: 转换为新维文（UYY）
    TO_IPA = BIT(8)         #: 转换为国际音标（IPA）
    REVERSE = BIT(9)        #: 还原操作（执行反操作）
    SYLLABLES = BIT(11)     #: 划分音节

    def __or__(self, other):
        return self.value | other.value

    def __and__(self, other):
        return self.value & other.value
