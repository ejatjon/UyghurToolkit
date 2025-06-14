#  这些字符是特殊字符，通常充当辅助角色
#  特殊字符 \uFE8C(ﺌ) \uFE8B(ﺋ) \uFEFC(ﻼ) \uFEFB(ﻻ)
#  当要输入 ئا ئۆ 等字符时，使用 ئ 代替 ﺌ  ﺋ
#  当要输入 ﻻ  时，使用 ل+ا
#  \uFEFC('ﻼ') 是 uFEFB('ﻻ') 的前连式 形式

SPECIAL_UEY_LATTER = {
    '_Hemze_':'\uFE8C',# ﺌ
    'Hemze_':'\uFE8B',# ﺋ
    '_La':'\uFEFC',# ﻼ
    'La':'\uFEFB',# ﻻ
    'Hemze':'\u0626',# ئ
}


def normalize_La(text:str) -> str:
    return text.replace('\uFEFB', '\u0644\u0627').replace('\uFEFC', '\u0644\u0627')

def normalize_Hemze(text:str) -> str:
    return text.replace('\uFE8C', '\u0626').replace('\uFE8B', '\u0626')
