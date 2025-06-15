"""
该模块包含新维文（UYY）相关的文本处理器，包括：
- 数字/日期转换处理器
- 符号转换处理器
- 音节划分处理器
- 转换到IPA,ULY,UKY,UEY字母的转换处理器
等核心处理功能
"""
import functools
import re
from typing import Union

from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.processor.Processor import Processor
from uyghur_toolkit.resources.dictionaries.letter_mapping.UYY_SCRIPTS import UYY_SCRIPTS
from uyghur_toolkit.resources.dictionaries.numbers import UYY_NUMBER_MAP, UYY_REVERSE_NUMBER_MAP
from uyghur_toolkit.resources.dictionaries.symbols import PUNCTUATIONS, UYY_SYMBOL_MAP
from uyghur_toolkit.resources.dictionaries.vowels import UYY_VOWELS
from uyghur_toolkit.utils.number_tools import decompose_number, decimal_places, decimal_number, toDecimal, divide


def is_vowel(s: str) -> bool:
    """
    判断是否是元音
    :param s: 字母
    :return: 布尔值，True为元音
    """
    if s in UYY_VOWELS:
        return True
    return False


def int_to_uyy(num: int) -> str:
    """
    将整数转换为UYY数字表示
    :param num: 整数
    :return: ULY数字表示的字符串
    """
    if num == 0:
        return UYY_NUMBER_MAP[0]
    components = decompose_number(num)
    result = []
    for unit, count in components:
        if unit == 1:  # 个位处理
            result.append(UYY_NUMBER_MAP[count])
        elif unit == 10:  # 十位处理（如20、30等）
            result.append(UYY_NUMBER_MAP[unit * count])
        else:  # 其他单位处理
            count_str = int_to_uyy(count)
            result.append(f"{count_str} {UYY_NUMBER_MAP[unit]}")
    return " ".join(result)


def float_to_uyy(num: float) -> str:
    """
    将浮点数转换为uly数字表示
    :param num: 浮点数
    :return: uly数字表示的浮点数字符串
    """
    integer_part = int_to_uyy(int(num))
    decimal_part = int_to_uyy(decimal_number(num))
    if decimal_part == '0':
        return integer_part
    decimal_places_count = decimal_places(num)
    decimal_places_unit = UYY_NUMBER_MAP.get(10 ** decimal_places_count, int_to_uyy(10 ** decimal_places_count))

    return f"{integer_part} pütün {decimal_places_unit} də {decimal_part}"


def number_hyphen_converter(s: str) -> str:
    """
    替换数字前的中划线（-），text是一个维语表示的数，此函数会给他添加 inchi 后缀
    :param s: 是一个维语表示的数
    :return: 替换后的字符串
    """
    s = list(s)
    if s[-1] == 'ə':
        s = s[:-1] + list('inqi')
    elif s[-1] == 'i':
        s = s[:-1] + list('inqi')
    else:
        s += 'inqi'
    return ''.join(s)


def number_hyphen_reverse(text: str):
    """
    匹配数字并替换为对应的维语表示
    :param text: 是一个字符串
    :return: 替换后的字符串
    """
    regex = re.compile(fr'''
    (\S+?)# 匹配非空字符（非贪婪）
    ({re.escape('inqi')})
    (?=\s|$) # 后边界检查（空格或结尾）
    ''', flags=re.VERBOSE | re.UNICODE | re.DOTALL)

    # 定义替换函数
    def replacement(match):
        """
        替换匹配的数字
        :param match: 匹配的match
        :return: 替换后的结果
        """
        prefix = match.group(1)
        if prefix in UYY_REVERSE_NUMBER_MAP.keys():
            return ' ' + prefix + ' - '
        elif prefix + 'i' in UYY_REVERSE_NUMBER_MAP.keys():
            return ' ' + prefix + 'i' + ' - '
        elif prefix + 'ə' in UYY_REVERSE_NUMBER_MAP.keys():
            return ' ' + prefix + 'ə' + ' - '
        else:
            return match.group(0)  # 默认不替换

    return regex.sub(replacement, text)


def uyy_punctuation_to_other(s: str, target: int) -> str:
    """
    将ULY标点符号转换成UEY,ULY,UKY,IPA 的标点符号
    :param s: 要转换的字符串
    :param target: 目标标点符号类型，值应为 0,1,3,4 (表示 UEY,ULY,UKY,IPA) 中的一个
    :return: 处理结果
    """
    if target not in [0, 1, 3, 4]:
        raise ValueError("Invalid target punctuation type")
    for punctuation in PUNCTUATIONS:
        s = s.replace(punctuation[2], punctuation[target])
    return s


class UYYNumberProcessor(Processor):
    """
    将数字转换为 UYY
    """

    def __init__(self, exclude_before: list[str] = None, exclude_after: list[str] = None, add_space: bool = True):
        """
        初始化参数
        :param exclude_before: 数字前缀，有此前缀的数字将被忽略
        :param exclude_after: 数字后缀，有此后缀的数字将被忽略
        :param add_space: 是否在匹配到的数字前后添加空格
        """
        super().__init__(ProcesClass.UYY, ProcesType.NUMBER, 'DefaultUYYNumberProcessor')
        if exclude_before is None:
            self.exclude_before = ['.', '-']
        else:
            self.exclude_before = exclude_before
        if exclude_after is None:
            self.exclude_after = ['-', '.', '/']
        else:
            self.exclude_after = exclude_after
        self.add_space = add_space

    def process(self, text: str):
        text = self.FloatNumber(text)
        text = self.IntegerNumber(text)
        return text

    def IntegerNumber(self, text: str) -> str:
        """
        将文本中的阿拉伯整数转换成 UYY 表示
        :param text: 要处理的字符串
        :return: 处理后的字符串
        """
        before_assertion, after_assertion = self._create_assertions()
        regex = re.compile(
            fr"""
                                    (?=\D|^) 
                                    (\D*?{before_assertion})
                                    (\d+)
                                    ({after_assertion}\D*?)
                                    (?=\D|$)
                                    """,
            re.VERBOSE | re.UNICODE | re.DOTALL)

        def replace(match):
            """
            替换匹配项
            :param match: 匹配项
            :return: 替换后的结果
            """
            # 解包捕获组
            prefix_part, number_str, suffix_part = match.groups()
            # 提取实际的前缀和后缀字符（去除断言部分）
            prefix = prefix_part.replace(before_assertion, '').strip()
            suffix = suffix_part.replace(after_assertion, '').strip()
            # 转换数字
            number = int_to_uyy(int(number_str))

            prefix, suffix = self._format_spaces(prefix, suffix)

            return f"{prefix}{number}{suffix}"

        return regex.sub(replace, text)

    def FloatNumber(self, text: str) -> str:
        """
        将文本中的阿拉伯小数转换成 UYY 表示
        :param text: 要处理的字符串
        :return: 处理后的字符串
        """
        before_assertion, after_assertion = self._create_assertions()

        regex = re.compile(
            fr"""
                                    (?=\D|^)
                                    (\D*?{before_assertion})
                                    (\d+\.\d+?)
                                    ({after_assertion}\D*?)
                                    (?=\D|$)
                                    """,
            re.VERBOSE | re.UNICODE | re.DOTALL)

        def replace(match):
            """
            替换匹配项
            :param match: 匹配项
            :return: 替换后的结果
            """
            # 解包捕获组
            prefix_part, number_str, suffix_part = match.groups()
            # 提取实际的前缀和后缀字符（去除断言部分）
            prefix = prefix_part.replace(before_assertion, '').strip()
            suffix = suffix_part.replace(after_assertion, '').strip()
            # 转换数字
            number = float_to_uyy(float(number_str))

            prefix, suffix = self._format_spaces(prefix, suffix)
            return f"{prefix}{number}{suffix}"

        return regex.sub(replace, text)

    def _format_spaces(self, prefix: str, suffix: str) -> tuple[str, str]:
        """
        如果 add_space 为真，则分别为数字前缀后和数字后缀前添加空格
        :param prefix: 数字前缀
        :param suffix: 数字后最
        :return: 处理后的字符串
        """
        if self.add_space:
            if prefix:
                prefix += ' ' if not prefix.endswith(' ') else ''
            else:
                prefix = ' '

            if suffix:
                suffix = (' ' + suffix) if not suffix.startswith(' ') else suffix
            else:
                suffix = ' '
        return prefix, suffix

    def _create_assertions(self) -> tuple[str, str]:
        """创建前后断言的正则表达式"""
        before_assertion = f'(?<!{"|".join(map(re.escape, self.exclude_before))})' if self.exclude_before else ''
        after_assertion = f'(?!{"|".join(map(re.escape, self.exclude_after))})' if self.exclude_after else ''
        return before_assertion, after_assertion


class UYYNumberReverseProcessor(Processor):
    """
    吧UYY 数字转换成阿拉伯数字,逻辑跟 UEY 样一。详细的内容参考 UEYNumberReverseProcessor
    """

    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.REVERSE | ProcesType.NUMBER, 'DefaultUYYNumberReverseProcessor')

    def process(self, text):
        text = self.reverse_float(text)
        return self.reverse_integer(text)

    def reverse_float(self, text: str):
        """
        将UYY 的小数转换成浮点数
        :param text: 转换的文本
        :return: 转换结果
        """
        prefix_str = 'pütün'
        suffix_str = 'də'
        result = []  # 结果
        pending_integer = []
        pending_decimal = []
        pending_order = []
        tokens = text.split()
        prefix, suffix = False, False
        for word in tokens:
            if word in UYY_REVERSE_NUMBER_MAP:
                if not prefix:
                    pending_integer.append(word)
                elif prefix and not suffix:
                    pending_order.append(word)
                else:
                    pending_decimal.append(word)
                continue
            elif word == prefix_str and not prefix:
                prefix = True
                continue
            elif word == suffix_str and prefix:
                suffix = True
                continue
            if prefix and suffix:
                integer_num = int(self.reverse_integer(' '.join(pending_integer)))
                decimal_num = int(self.reverse_integer(' '.join(pending_decimal)))
                order_num = int(self.reverse_integer(' '.join(pending_order)))
                total = toDecimal(integer_num) + divide(decimal_num, order_num)
                result.append('%s' % total)
            else:
                result += pending_integer + pending_order + pending_decimal
            pending_integer, pending_order, pending_decimal = [], [], []
            prefix, suffix = False, False
            result.append(word)
        if prefix and suffix:
            integer_num = int(self.reverse_integer(' '.join(pending_integer)))
            decimal_num = int(self.reverse_integer(' '.join(pending_decimal)))
            order_num = int(self.reverse_integer(' '.join(pending_order)))
            total = toDecimal(integer_num) + divide(decimal_num, order_num)
            result.append('%s' % total)
        else:
            result += pending_integer + pending_order + pending_decimal
        return " ".join(result)

    def reverse_integer(self, text: str) -> str:
        """
        吧维语整数转换成阿拉伯数
        :param text: 要转换的文本
        :return: 转换结果
        """
        result = []  # 结果
        pending = []  # 暂存数字
        tokens = text.split()
        for word in tokens:
            if word in UYY_REVERSE_NUMBER_MAP:
                pending.append((UYY_REVERSE_NUMBER_MAP[word], UYY_REVERSE_NUMBER_MAP[word] < 100))
                continue
            if pending:
                result.append(str(sum([self.evaluate_subarray(i) for i in self.split_array(pending)])))
                pending = []
            result.append(word)
        if pending:
            result.append(str(sum([self.evaluate_subarray(i) for i in self.split_array(pending)])))
        return " ".join(result)

    def split_array(self, arr: list[tuple[int, bool]]):
        """
        吧数字列表分成几个数量级单调递增的部分
        :param arr: 数字列表
        :return: 单调递增的数字列表的列表
        """
        if not arr:
            return []
        max_val = -1
        split_index = -1
        for i, (num, is_p) in enumerate(arr):
            if not is_p and num > max_val:  # 只处理False（c）元素
                max_val = num
                split_index = i

        if split_index == -1:
            # 没有数量级（100，1000 ...）元素时，每个元素单独成组
            return [[elem] for elem in arr]

        left = arr[:split_index + 1]
        right = arr[split_index + 1:]
        return [left] + self.split_array(right)

    @staticmethod
    def evaluate_subarray(subarray):
        """
        整合单调递增的数字列表
        :param subarray: 单调递增的数字列表
        :return: 整合结果
        """
        if not subarray:
            return 0
        # 初始值为第一个元素
        current = subarray[0][0]
        for num, is_p in subarray[1:]:
            if is_p:
                current += num  # p/c -> p: 加法
            else:
                current *= num  # p/c -> c: 乘法
        return current


class UYYDateProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.DATE, 'DefaultUYYDateProcessor')
        self.date_regex_map = {
            'iso': {  # 格式1：YYYY-MM-DD
                'regex_year': r'\d{1,4}',
                'regex_month': r'0?[1-9]|1[0-2]',
                'regex_day': r'0?[1-9]|[12]\d|3[01]',
                'regex_separator': r'-',
                'handler': self.default_handler,
            },
            'slash': {  # 格式2：YYYY/MM/DD
                'regex_year': r'\d{1,4}',
                'regex_month': r'0?[1-9]|1[0-2]',
                'regex_day': r'0?[1-9]|[12]\d|3[01]',
                'regex_separator': r'/',
                'handler': self.default_handler,
            },
            'dot': {  # 格式3：YYYY.MM.DD
                'regex_year': r'\d{1,4}',
                'regex_month': r'0?[1-9]|1[0-2]',
                'regex_day': r'0?[1-9]|[12]\d|3[01]',
                'regex_separator': r'\.',
                'handler': self.default_handler,
            }
        }

    def process(self, s: str) -> str:
        def replace_handler(match: re.Match):
            """
            替换处理函数
            :param match: 匹配对象
            :return: 替换后的字符串
            """
            handle = self.date_regex_map[match.lastgroup].get('handler', self.default_handler)
            year, month, day = handle(match.lastgroup, match)
            year_unit = 'yili'
            month_unit = 'ayning'
            day_unit = 'küni'
            return f"{self.convert_date_number(year)} {year_unit}"\
                   f" {self.convert_date_number(month)} {month_unit} {self.convert_date_number(day)} {day_unit}"

        return self.mk_regex().sub(replace_handler, s)

    @staticmethod
    def convert_date_number(s):
        """
        输入数字，返回维语数字
        :param s: 数字
        :return: 维语数字
        """
        number = int(s)
        uyy_number = int_to_uyy(number)
        return number_hyphen_converter(uyy_number)

    def mk_regex(self):
        """
        创建正则
        :return: 正则
        """
        regex_list = []
        for k, v in self.date_regex_map.items():
            regex_year = rf"(?P<{k}_year>{v['regex_year']})"
            regex_month = rf"(?P<{k}_month>{v['regex_month']})"
            regex_day = rf"(?P<{k}_day>{v['regex_day']})"
            regex_separator = v['regex_separator']
            regex_str = rf"(?P<{k}>{regex_year}{regex_separator}{regex_month}{regex_separator}{regex_day})"
            regex_list.append(regex_str)

        return re.compile(rf"(?<!\d)(?:{'|'.join(regex_list)})(?!\d)", flags=re.VERBOSE | re.UNICODE | re.DOTALL)

    @staticmethod
    def default_handler(class_name: str, m: re.Match) -> tuple[str, str, str]:
        """
        默认处理函数
        :param class_name: 处理类名
        :param m: 匹配对象
        :return: 处理结果
        """
        return m.group(f'{class_name}_year'), m.group(f'{class_name}_month'), m.group(f'{class_name}_day')


class UYYDateAndNumberReverseProcessor(Processor):
    """
    日期和数字转换
    """

    def __init__(self):
        super().__init__(ProcesClass.UYY,
                         ProcesType.REVERSE | ProcesType.DATE | ProcesType.NUMBER,
                         'DefaultUYYDateAndNumberReverseProcessor')
        self.number_reverse = UYYNumberReverseProcessor()

    def process(self, text: str, separators: str = '-'):
        regex = re.compile(fr"(\d+)(\s*-\s* {re.escape('yili')} \s*)"
                           rf"(\d+)(\s*-\s* {re.escape('ayning')} \s*)"
                           rf"(\d+)(\s*-\s* {re.escape('küni')} \s*)",
                           flags=re.VERBOSE | re.UNICODE | re.DOTALL)

        def replacement(match: re.Match):
            """
            替换匹配项
            :param match: 匹配项
            :return: 替换后的结果
            """
            year_num = match.group(1)
            month_num = match.group(3)
            day_num = match.group(5)
            return f" {year_num} {separators} {month_num} {separators} {day_num} "

        text = number_hyphen_reverse(text)
        text = self.number_reverse.process(text)
        return regex.sub(replacement, text)


class UYYNormalizeProcessor(Processor):

    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.NORMALIZATION, 'DefaultUYYNormalizeProcessor')

    def process(self, text: str):
        return text.lower()


class UYYNormalizeReverseProcessor(Processor):

    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.REVERSE | ProcesType.NORMALIZATION,
                         'DefaultUYYNormalizeReverseProcessor')

    def process(self, text: str) -> str:
        """
        将标准化的字符串，恢复成原始书写形式
        :param text:
        :return:
        """
        return text.capitalize()


class UYYSymbolsProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.SYMBOL, "DefaultUYYSymbolsProcessor")

    def process(self, text: str) -> str:
        for k, v in UYY_SYMBOL_MAP.items():
            text = text.replace(k, v)
        return text


class UYYSymbolsReverseProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.SYMBOL | ProcesType.REVERSE, "DefaultUYYSymbolsReverseProcessor")

    def process(self, text: str) -> str:
        for k, v in UYY_SYMBOL_MAP.items():
            text = text.replace(v, k)
        return text


class UYYToIPAProcessor(Processor):
    """
    UYY 转换到 IPA
    """

    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.TO_IPA, "DefaultUYYToIPAProcessor")

    def process(self, text: str) -> str:
        """
        将UYY字符串转换成IPA字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower().split()
        result = []
        for word in text:
            result.append(self.convertToIPA(word))
        return uyy_punctuation_to_other(' '.join(result), 4)

    @staticmethod
    def convertToIPA(word: str):
        """
        将UYY字符串转换成IPA字符串。
        :param word: 要转换的文本
        :return: 处理结果
        """
        result = []
        pending_char = ''
        for c in word:
            if not pending_char:
                pending_char = c
            forms = UYY_SCRIPTS.get(pending_char + c, None)
            if forms:
                result.append(forms['IPA'][0])
                pending_char = ''
            else:
                result.append(pending_char)
                pending_char = c
        forms = UYY_SCRIPTS.get(pending_char, None)
        result.append(forms['IPA'][0] if forms else pending_char)
        return ''.join(result)


class UYYToUKYProcessor(Processor):
    """
    UYY 转换到 UKY
    """

    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.TO_UKY, 'DefaultUYYToUKYProcessor')

    def process(self, text: str) -> str:
        """
        将UYY字符串转换成UKY字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower().split()
        result = []
        for word in text:
            result.append(self.convertToUKY(word))
        return uyy_punctuation_to_other(' '.join(result), 3)

    @staticmethod
    def convertToUKY(word: str):
        """
        将UYY字符串转换成UKY字符串。
        :param word: 要转换的字符串
        :return: 处理结果
        """
        result = []
        pending_char = ''
        for c in word:
            if not pending_char:
                pending_char = c
            forms = UYY_SCRIPTS.get(pending_char + c, None)
            if forms:
                result.append(forms['UKY']['other'])
                pending_char = ''
            else:
                result.append(pending_char)
                pending_char = c
        forms = UYY_SCRIPTS.get(pending_char, None)
        result.append(forms['UKY']['other'] if forms else pending_char)
        return ''.join(result).replace('й‍‍у', '\u044e').replace('йa', '\u044f')  # 处理 ю、я


class UYYToUEYProcessor(Processor):
    """
    UYY 转换到 UEY
    """

    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.TO_UEY, 'DefaultUYYToUEYProcessor')
        self.uyy_divide_syllables_processor = UYYDivideSyllablesProcessor()
        self.hemze = '\u0626'

    def process(self, text: str) -> str:
        """
        将ULY字符串转换成IPA字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower()
        text = self.uyy_divide_syllables_processor.process(text=text, delimiter='<dlmt>').split('<dlmt>')
        result = []
        for word in text:
            word = self.add_Hemze(word)
            result.append(self.convertToUEY(word))
        return uyy_punctuation_to_other(' '.join(result), 0)

    @staticmethod
    def convertToUEY(word: str) -> str:
        """
        将UYY格式的词转换为UEY格式
        :param word:
        :return:
        """
        result = []
        pending_char = ''
        for c in word:
            if not pending_char:
                pending_char = c
                continue
            forms = UYY_SCRIPTS.get(pending_char + c, None)
            if forms:
                result.append(forms['UEY']['Base'])
                pending_char = ''
            else:
                forms = UYY_SCRIPTS.get(pending_char, None)
                if forms:
                    result.append(forms['UEY']['Base'])
                    pending_char = c
                else:
                    result.append(pending_char)
                    pending_char = c
        forms = UYY_SCRIPTS.get(pending_char, None)
        result.append(forms['UEY']['Base'] if forms else pending_char)
        return ''.join(result)

    def add_Hemze(self, word_syllables: str) -> str:
        """
        将 Uyghur(维吾尔语) 单词中的音节开头的元音字母加上hemze 隔音字符
        :param word_syllables: 要处理的 Uyghur(维吾尔语)单词以空格划分的音节
        :return: 处理后的 Uyghur(维吾尔语) 单词
        """
        result = []
        for i in word_syllables.split():
            if is_vowel(i[0]):
                result.append(self.hemze + i)
            else:
                result.append(i)
        return ''.join(result)


class UYYToULYProcessor(Processor):
    """
    UYY 转换到 ULY
    """

    def __init__(self):
        super().__init__(ProcesClass.UYY, ProcesType.TO_UEY, 'DefaultUYYToULYProcessor')
        self.uyy_divide_syllables_processor = UYYDivideSyllablesProcessor()
        self.right_single_quotation_mark = '\u2019'  # (’,\u2019 ) 分割符

    def process(self, text: str) -> str:
        """
        将UYY字符串转换成ULY字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower()
        text = self.uyy_divide_syllables_processor.process(text=text, delimiter='<dlmt>').split('<dlmt>')
        result = []
        for word in text:
            word = self.add_Apostrophe(word)
            result.append(self.convertToULY(word))
        return uyy_punctuation_to_other(' '.join(result), 1)

    def convertToULY(self, word: str) -> str:
        """
        将UYY字符串转换为ULY字符串
        :param word: UYY字符串
        :return: ULY字符串
        """
        result = ''
        pending_char = ''
        for c in word:
            if not pending_char:
                pending_char = c
                continue
            forms = UYY_SCRIPTS.get(pending_char + c, None)
            if forms:
                if result[-1] + forms['ULY']['other'] in ['gh', 'ng', 'sh', 'zh']:
                    result += self.right_single_quotation_mark + forms['ULY']['other']
                else:
                    result += forms['ULY']['other']
                pending_char = ''
            else:
                forms = UYY_SCRIPTS.get(pending_char, None)
                if forms:
                    result += forms['ULY']['other']
                    pending_char = c
                else:
                    result += pending_char
                    pending_char = c
        forms = UYY_SCRIPTS.get(pending_char, None)
        result += forms['ULY']['other'] if forms else pending_char
        return ''.join(result)

    def add_Apostrophe(self, word_syllables: str) -> str:
        """
        将维语单词中的音节开头的元音前面一个音节最后一个字母为辅音，则字母加上 (’,\u2019 ) 隔音字符
        :param word_syllables: 要处理的 Uyghur(维吾尔语)单词以空格划分的音节
        :return: 处理后的 Uyghur(维吾尔语) 单词
        """
        result = []
        prev_syllables = ""
        for i in word_syllables.split():
            if not prev_syllables:
                prev_syllables = i
                continue
            if is_vowel(i[0]) and not is_vowel(prev_syllables[-1]):
                result.append(self.right_single_quotation_mark + i)
            else:
                result.append(i)
            prev_syllables = i
        return ''.join(result)


class UYYDivideSyllablesProcessor(Processor):
    """
    UYY 音节划分
    具体逻辑参考了论文《现代维吾尔文音节自动切分方法及其实现》(瓦依提.阿不力孜,加米拉.吾守尔,吐尔根.依布拉音,阿依佐克拉.瓦依提)
    原始算法在反向遍历时 当遇到两个并列元音（VV）时并不会切分，只当遇到 VC 时进行切分，这样在文本中出现多个外来词时 音节的划分可能会更加准确。
    但在这里默认会切分 两个并列元音（VV） 这样使得，大部分情况下的音节划分可能更加准确
    """

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.SYLLABLES, 'DefaultUYYDivideSyllablesProcessor')
        self.syllables_form = ['V', 'VC', 'CV', 'CVC', 'VCC', 'CVCC', 'CCV', 'CCVC', 'CCVCC', 'CVV', 'CVVC',
                               'CCCV']

    def process(self, text: str, split_vowels: bool = True, delimiter: str = ''):
        """
        划分音节。因为UYY中没有hemze，
        因此需要对UEYDivideSyllablesProcessor中的处理逻辑中去掉按照hemze分割的逻辑。
        :param text: 需要处理的文字
        :param split_vowels: 是否切割两个并列元音(VV)。如果文字中包含了太多汉语借词时可以设置成False
        :param delimiter: 词之间的分隔符
        :return: 转换后的音节字符串
        """
        syllable_list = []
        for word in text.split():
            word = self.mk_Letter_List(word)
            # 元音辅音（vowel consonants）二元列表，v 表示元音，c 表示辅音
            v_c_list = []
            for c in word:
                if is_vowel(c):
                    v_c_list.append('V')
                else:
                    v_c_list.append('C')
            v_c_list = self.reverseIterateSyllable(v_c_list, split_vowels)
            index = 0
            # 正向遍历并纠正音节
            while index < len(v_c_list):
                if (v_c_list[index] not in self.syllables_form) and (index < len(v_c_list) - 1):
                    new_syllable = self.iterateSyllable(v_c_list[index] + v_c_list[index + 1])
                    if new_syllable:
                        v_c_list[index:index + 2] = new_syllable
                        index += len(new_syllable)
                    else:
                        v_c_list[index:index + 2] = [v_c_list[index] + v_c_list[index + 1]]
                else:
                    index += 1
            block_syllable_list = []
            index = 0
            for i in v_c_list:
                syllable = word[index:index + len(i)]
                block_syllable_list.append(''.join(syllable))
                index += len(i)

            syllable_list.append(' '.join(block_syllable_list))
        return f' {delimiter} '.join(syllable_list)

    @staticmethod
    def mk_Letter_List(word: str) -> list[str]:
        """
        创建字母列表
        :param word: 单词
        :return: 字母列表
        """

        result = []
        word += ' ' + ' '  # 添加两个空格
        prev_char = word[0]
        index = 1
        while len(word) - 1 > index:
            if prev_char + word[index] in ['ng']:
                result.append(prev_char + word[index])
                prev_char = word[index + 1]  # 因为添加了两个空格，因此如果执行到这里说明index+1 不为' ' 因此index+2 必存在
                index += 2
                continue
            else:
                result.append(prev_char)
                prev_char = word[index]
            index += 1
        return result

    @staticmethod
    def reverseIterateSyllable(v_c_list: list[str], split_vowels: bool) -> list[str]:
        """
        反向便利并切分音节
        :param v_c_list: 元音辅音（vowel consonants）二元列表，v 表示元音，c 表示辅音
        :param split_vowels: 是否切割两个并列元音(VV)。
        例如split_vowels为True时遇到 CVVC 这样的音节时，会分割成CV VC,False 时CVVC。
        如果文字中包含了太多汉语借词时可以设置成False
        :return: 音节列表
        """

        prev_letter_is_vowel = False
        pending = ''
        syllable_list = []
        for i in v_c_list[::-1]:
            if i == 'V':
                if prev_letter_is_vowel:
                    if split_vowels:
                        syllable_list.append(pending)
                        pending = 'V'
                    else:
                        pending = 'V' + pending
                else:
                    pending = 'V' + pending
                    prev_letter_is_vowel = True
            else:
                if prev_letter_is_vowel:
                    syllable_list.append('C' + pending)
                    pending = ''
                    prev_letter_is_vowel = False
                else:
                    pending = 'C' + pending
        if pending:
            syllable_list.append(pending)
        return syllable_list[::-1]

    @functools.lru_cache(maxsize=None)
    def iterateSyllable(self, block: str) -> Union[list[str], None]:
        """
        正向遍历并切分音节
        :param block: VC 块
        :return: 音节列表 或 None
        """
        if block in self.syllables_form:
            return [block]
        for i in self.syllables_form:
            if len(i) >= len(block):
                continue
            if i == block[:len(i)] and self.iterateSyllable(block[len(i):]):
                return [i] + self.iterateSyllable(block[len(i):])
        return None
