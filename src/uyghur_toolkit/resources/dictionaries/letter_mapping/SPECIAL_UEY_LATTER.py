#  这些字符是特殊字符，通常充当辅助角色
#  特殊字符 \uFE8C(ﺌ) \uFE8B(ﺋ) \uFEFC(ﻼ) \uFEFB(ﻻ)
#  当要输入 ئا ئۆ 等字符时，使用 ئ 代替 ﺌ  ﺋ
#  当要输入 ﻻ  时，使用 ل+ا
#  \uFEFC('ﻼ') 是 uFEFB('ﻻ') 的前连式 形式

SPECIAL_UEY_LATTER = [
    'ﺌ',# \uFE8C
    'ﺋ',# \uFE8B
    'ﻼ',# \uFEFC
    'ﻻ',# \uFEFB
    'ئ',# \u0626
]

