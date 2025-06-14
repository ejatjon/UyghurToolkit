import enum
from uyghur_toolkit.utils.other import BIT

"""
任何处理逻辑需要实现Processor（处理器）类，
ProcessorType 处理器属性，如 NORMALIZATION | REVERSE 表示处理恢复标准化的字符（标准化的反操作）
ProcessorType 通过组合 REVERSE 表示反向操作
"""


class ProcesType(enum.IntEnum):
    UNDEFINED           = 0
    NORMALIZATION       = BIT(0)   # 文本标准化处理（统一字符形式）
    NUMBER              = BIT(1)   # 数字格式转换（如：阿拉伯数字↔维文数字）
    SYMBOL              = BIT(2)   # 符号格式转换（标点符号/货币符号等）
    DATE                = BIT(3)   # 日期格式转换（数字公历↔维文
    TO_UEY              = BIT(4)   # 转换为老维文（UEY）
    TO_UKY              = BIT(5)   # 转换为西里尔维文（UKY）
    TO_ULY              = BIT(6)   # 转换为拉丁维文（ULY）
    TO_UYY              = BIT(7)   # 转换为新维文（UYY）
    TO_IPA              = BIT(8)   # 转换为国际音标（IPA）
    REVERSE             = BIT(9)   # 还原 (将进行反操作)
    SYLLABLES           = BIT(11)  # 划分音节（不可还原）

    def __or__(self, other):
        return self.value | other.value

    def __and__(self, other):
        return self.value & other.value





