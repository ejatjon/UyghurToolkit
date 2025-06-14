import enum
from enum import auto




@enum.unique
class ProcesClass(enum.Enum):
    UNDEFINED= auto()
    UEY= auto()    # 老维文（UEY）
    ULY= auto()    # 拉丁维文（ULY）
    UYY= auto()    # 新维文（UYY）
    UKY= auto()    # 西里尔维文（UKY）
    IPA= auto()    # 国际音标（IPA
