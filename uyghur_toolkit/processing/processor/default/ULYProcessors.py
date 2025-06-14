import functools
import re

from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.processor.Processor import Processor
from uyghur_toolkit.resources.dictionaries.letter_mapping.ULY_SCRIPTS import ULY_SCRIPTS
from uyghur_toolkit.resources.dictionaries.numbers import ULY_NUMBER_MAP, ULY_REVERSE_NUMBER_MAP
from uyghur_toolkit.resources.dictionaries.symbols import PUNCTUATIONS, ULY_SYMBOL_MAP
from uyghur_toolkit.resources.dictionaries.vowels import ULY_VOWELS
from uyghur_toolkit.utils.number_tools import decompose_number, decimal_number, decimal_places, toDecimal, divide


def is_vowel(s: str) -> bool:
    if s in ULY_VOWELS:
        return True
    return False


def int_to_uly(num: int) -> str:
    """
    将整数转换为ULY数字表示
    :param num: 整数
    :return: ULY数字表示的字符串
    """
    if num == 0:
        return ULY_NUMBER_MAP[0]
    components = decompose_number(num)
    result = []
    for unit, count in components:
        if unit == 1:  # 个位处理
            result.append(ULY_NUMBER_MAP[count])
        elif unit == 10:  # 十位处理（如20、30等）
            result.append(ULY_NUMBER_MAP[unit * count])
        else:  # 其他单位处理
            count_str = int_to_uly(count)
            result.append(f"{count_str} {ULY_NUMBER_MAP[unit]}")
    return " ".join(result)


def float_to_uly(num: float) -> str:
    """
    将浮点数转换为uly数字表示
    :param num: 浮点数
    :return: uly数字表示的浮点数字符串
    """
    integer_part = int_to_uly(int(num))
    decimal_part = int_to_uly(decimal_number(num))
    if decimal_part == '0':
        return integer_part
    decimal_places_count = decimal_places(num)
    decimal_places_unit = ULY_NUMBER_MAP.get(10 ** decimal_places_count, int_to_uly(10 ** decimal_places_count))

    return f"{integer_part} pütün {decimal_places_unit} de {decimal_part}"


def number_hyphen_converter(s: str) -> str:
    """
    替换数字前的中划线（-），text是一个维语表示的数，此函数会给他添加 inchi 后缀
    :param s: 是一个维语表示的数
    :return: 替换后的字符串
    """
    s = list(s)
    if s[-1] == 'e':
        s = s[:-1] + list('inchi')
    elif s[-1] == 'i':
        s = s[:-1] + list('inchi')
    else:
        s += 'inchi'
    return ''.join(s)


def number_hyphen_reverse(text: str):
    regex = re.compile(fr'''
    (\S+?)# 匹配非空字符（非贪婪）
    ({re.escape('inchi')})
    (?=\s|$) # 后边界检查（空格或结尾）
    ''', flags=re.VERBOSE | re.UNICODE | re.DOTALL)

    # 定义替换函数
    def replacement(match):
        prefix = match.group(1)
        if prefix in ULY_REVERSE_NUMBER_MAP.keys():
            return ' ' + prefix + ' - '
        elif prefix + 'i' in ULY_REVERSE_NUMBER_MAP.keys():
            return ' ' + prefix + 'i' + ' - '
        elif prefix + 'e' in ULY_REVERSE_NUMBER_MAP.keys():
            return ' ' + prefix + 'e' + ' - '
        else:
            return match.group(0)  # 默认不替换

    return regex.sub(replacement, text)


def uly_punctuation_to_other(s: str, target: int) -> str:
    """
    将ULY标点符号转换成UEY,UYY,UKY,IPA 的标点符号
    :param s: 要转换的字符串
    :param target: 目标标点符号类型，值应为 0,2,3,4 (表示 UEY,UYY,UKY,IPA) 中的一个
    :return: 处理结果
    """
    if target not in [0, 2, 3, 4]:
        raise ValueError("Invalid target punctuation type")
    for punctuation in PUNCTUATIONS:
        s = s.replace(punctuation[1], punctuation[target])
    return s


class ULYNumberProcessor(Processor):
    def __init__(self, exclude_before: list[str] = None, exclude_after: list[str] = None, add_space: bool = True):
        """
        初始化参数
        :param exclude_before: 数字前缀，有此前缀的数字将被忽略
        :param exclude_after: 数字后缀，有此后缀的数字将被忽略
        :param add_space: 是否在匹配到的数字前后添加空格
        """
        super().__init__(ProcesClass.ULY, ProcesType.NUMBER,'DefaultULYNumberProcessor')
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
        将文本中的阿拉伯整数转换成 ULY 表示
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
            # 解包捕获组
            prefix_part, number_str, suffix_part = match.groups()
            # 提取实际的前缀和后缀字符（去除断言部分）
            prefix = prefix_part.replace(before_assertion, '').strip()
            suffix = suffix_part.replace(after_assertion, '').strip()
            # 转换数字
            number = int_to_uly(int(number_str))

            prefix, suffix = self._format_spaces(prefix, suffix)

            return f"{prefix}{number}{suffix}"

        return regex.sub(replace, text)

    def FloatNumber(self, text: str) -> str:
        """
        将文本中的阿拉伯小数转换成 ULY 表示
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
            # 解包捕获组
            prefix_part, number_str, suffix_part = match.groups()
            # 提取实际的前缀和后缀字符（去除断言部分）
            prefix = prefix_part.replace(before_assertion, '').strip()
            suffix = suffix_part.replace(after_assertion, '').strip()
            # 转换数字
            number = float_to_uly(float(number_str))

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


class ULYNumberReverseProcessor(Processor):
    """
    吧ULY 数字转换成阿拉伯数字,逻辑跟 UEY 样一。详细的内容参考 UEYNumberReverseProcessor
    """

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.REVERSE | ProcesType.NUMBER, 'DefaultULYNumberReverseProcessor')

    def process(self, text):
        text = self.reverse_float(text)
        return self.reverse_integer(text)

    def reverse_float(self, text: str):
        """
        将ULY 的小数转换成浮点数
        :param text: 转换的文本
        :return: 转换结果
        """
        prefix_str = 'pütün'
        suffix_str = 'de'
        result = []  # 结果
        pending_integer = []
        pending_decimal = []
        pending_order = []
        tokens = text.split()
        prefix, suffix = False, False
        for word in tokens:
            if word in ULY_REVERSE_NUMBER_MAP:
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
            if word in ULY_REVERSE_NUMBER_MAP:
                pending.append((ULY_REVERSE_NUMBER_MAP[word], ULY_REVERSE_NUMBER_MAP[word] < 100))
                continue
            if pending:
                result.append(str(sum([self.evaluate_subarray(i) for i in self.split_array(pending)])))
                pending = []
            result.append(word)
        if pending:
            result.append(str(sum([self.evaluate_subarray(i) for i in self.split_array(pending)])))
        return " ".join(result)

    def split_array(self, arr: list[tuple[int, bool]]):
        '''
        吧数字列表分成几个数量级单调递增的部分
        :param arr: 数字列表
        :return: 单调递增的数字列表的列表
        '''
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


class ULYDateProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.DATE,'DefaultULYDateProcessor')
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
            handle = self.date_regex_map[match.lastgroup].get('handler', self.default_handler)
            year, month, day = handle(match.lastgroup, match)
            year_unit = 'yili'
            month_unit = 'ayning'
            day_unit = 'küni'
            return f"{self.convert_date_number(year)} {year_unit} {self.convert_date_number(month)} {month_unit} {self.convert_date_number(day)} {day_unit}"

        return self.mk_regex().sub(replace_handler, s)

    @staticmethod
    def convert_date_number(s):
        number = int(s)
        uly_number = int_to_uly(number)
        return number_hyphen_converter(uly_number)

    def mk_regex(self):
        regex_list = []
        for k, v in self.date_regex_map.items():
            regex_year = rf'(?P<{k}_year>{v['regex_year']})'
            regex_month = rf'(?P<{k}_month>{v['regex_month']})'
            regex_day = rf'(?P<{k}_day>{v['regex_day']})'
            regex_separator = v['regex_separator']
            regex_str = rf'(?P<{k}>{regex_year}{regex_separator}{regex_month}{regex_separator}{regex_day})'
            regex_list.append(regex_str)

        return re.compile(rf'(?<!\d)(?:{'|'.join(regex_list)})(?!\d)', flags=re.VERBOSE | re.UNICODE | re.DOTALL)

    @staticmethod
    def default_handler(class_name: str, m: re.Match) -> tuple[str, str, str]:
        return m.group(f'{class_name}_year'), m.group(f'{class_name}_month'), m.group(f'{class_name}_day')


class ULYDateAndNumberReverseProcessor(Processor):

    def __init__(self):
        super().__init__(ProcesClass.ULY,
                         ProcesType.REVERSE | ProcesType.DATE | ProcesType.NUMBER, 'DefaultULYDateAndNumberReverseProcessor')
        self.number_reverse = ULYNumberReverseProcessor()

    def process(self, text: str, separators: str = '-'):
        regex = re.compile(fr'''
                (\d+)(\s*-\s* {re.escape('yili')} \s*)(\d+)(\s*-\s* {re.escape('ayning')} \s*)(\d+)(\s*-\s* {re.escape('küni')} \s*)        # year month day        
                ''', flags=re.VERBOSE | re.UNICODE | re.DOTALL)

        def replacement(match):
            year_num = match.group(1)
            month_num = match.group(3)
            day_num = match.group(5)
            return f" {year_num} {separators} {month_num} {separators} {day_num} "

        text = number_hyphen_reverse(text)
        text = self.number_reverse.process(text)
        return regex.sub(replacement, text)


class ULYNormalizeProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.NORMALIZATION, "DefaultULYNormalizeProcessor")

    def process(self, text: str):
        return text.lower()


class ULYNormalizeReverseProcessor(Processor):

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.REVERSE | ProcesType.NORMALIZATION, "DefaultULYNormalizeReverseProcessor")

    def process(self, text: str) -> str:
        """
        将标准化的字符串，恢复成原始书写形式
        :param text:
        :return:
        """
        return text.capitalize()


class ULYSymbolsProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.SYMBOL, "DefaultULYSymbolsProcessor")

    def process(self, text: str) -> str:
        for k, v in ULY_SYMBOL_MAP.items():
            text = text.replace(k, v)
        return text


class ULYSymbolsReverseProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.SYMBOL | ProcesType.REVERSE, "DefaultULYSymbolsReverseProcessor")

    def process(self, text: str) -> str:
        for k, v in ULY_SYMBOL_MAP.items():
            text = text.replace(v, k)
        return text


class ULYToUYYProcessor(Processor):
    """
    ULY 转换到 UYY
    """

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.TO_UYY, "DefaultULYToUYYProcessor")
        self.right_single_quotation_mark = '\u2019'  # (’,\u2019 ) 分割符

    def process(self, text: str) -> str:
        """
        将ULY字符串转换成UYY字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower().split()
        result = []
        for word in text:
            result.append(self.convertToUYY(word))
        return uly_punctuation_to_other(' '.join(result), 2)

    def convertToUYY(self, word: str):
        word = word.split(self.right_single_quotation_mark)
        result = []
        for substr in word:
            pending_char = ''
            for c in substr:
                if not pending_char:
                    pending_char = c
                forms = ULY_SCRIPTS.get(pending_char + c, None)
                if forms:
                    result.append(forms['UYY']['other'])
                    pending_char = ''
                else:
                    result.append(pending_char)
                    pending_char = c
            forms = ULY_SCRIPTS.get(pending_char, None)
            result.append(forms['UYY']['other'] if forms else pending_char)
        return ''.join(result)


class ULYToIPAProcessor(Processor):
    """
    ULY 转换到 IPA
    """

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.TO_IPA, 'DefaultULYToIPAProcessor')
        self.right_single_quotation_mark = '\u2019'  # (’,\u2019 ) 分割符

    def process(self, text: str) -> str:
        """
        将ULY字符串转换成IPA字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower().split()
        result = []
        for word in text:
            result.append(self.convertToIPA(word))
        return uly_punctuation_to_other(' '.join(result), 4)

    def convertToIPA(self, word: str):
        word = word.split(self.right_single_quotation_mark)
        result = []
        for substr in word:
            pending_char = ''
            for c in substr:
                if not pending_char:
                    pending_char = c
                forms = ULY_SCRIPTS.get(pending_char + c, None)
                if forms:
                    result.append(forms['IPA'][0])
                    pending_char = ''
                else:
                    result.append(pending_char)
                    pending_char = c
            forms = ULY_SCRIPTS.get(pending_char, None)
            result.append(forms['IPA'][0] if forms else pending_char)
        return ''.join(result)


class ULYToUKYProcessor(Processor):
    """
    ULY 转换到 UKY
    """

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.TO_UKY, 'DefaultULYToUKYProcessor')
        self.right_single_quotation_mark = '\u2019'  # (’,\u2019 ) 分割符

    def process(self, text: str) -> str:
        """
        将ULY字符串转换成UKY字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower().split()
        result = []
        for word in text:
            result.append(self.convertToUKY(word))
        return uly_punctuation_to_other(' '.join(result), 3)

    def convertToUKY(self, word: str):
        word = word.split(self.right_single_quotation_mark)
        result = []
        for substr in word:
            pending_char = ''
            for c in substr:
                if not pending_char:
                    pending_char = c
                forms = ULY_SCRIPTS.get(pending_char + c, None)
                if forms:
                    result.append(forms['UKY']['other'])
                    pending_char = ''
                else:
                    result.append(pending_char)
                    pending_char = c
            forms = ULY_SCRIPTS.get(pending_char, None)
            result.append(forms['UKY']['other'] if forms else pending_char)
        return ''.join(result).replace('й‍‍у', '\u044e').replace('йa', '\u044f')  # 处理 ю、я


class ULYToUEYProcessor(Processor):
    """
    ULY 转换到 UKY
    """

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.TO_UEY, 'DefaultULYToUEYProcessor')
        self.uly_divide_syllables_processor = ULYDivideSyllablesProcessor()
        self.right_single_quotation_mark = '\u2019'  # (’,\u2019 ) 分割符
        self.hemze = '\u0626'

    def process(self, text: str) -> str:
        """
        将ULY字符串转换成IPA字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = text.lower()
        text = self.uly_divide_syllables_processor.process(text=text, delimiter='<dlmt>').split('<dlmt>')
        result = []
        for word in text:
            word = self.add_Hemze(word)
            result.append(self.convertToUEY(word))
        return uly_punctuation_to_other(' '.join(result), 0)

    def convertToUEY(self, word: str):
        word = word.split(self.right_single_quotation_mark)
        result = []
        for substr in word:
            pending_char = ''
            for c in substr:
                if not pending_char:
                    pending_char = c
                    continue
                forms = ULY_SCRIPTS.get(pending_char + c, None)
                if forms:
                    result.append(forms['UEY']['Base'])
                    pending_char = ''
                else:
                    forms = ULY_SCRIPTS.get(pending_char, None)
                    if forms:
                        result.append(forms['UEY']['Base'])
                        pending_char = c
                    else:
                        result.append(pending_char)
                        pending_char = c
            forms = ULY_SCRIPTS.get(pending_char, None)
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


class ULYDivideSyllablesProcessor(Processor):
    """
    ULY 音节划分
    具体逻辑参考了论文《现代维吾尔文音节自动切分方法及其实现》(瓦依提.阿不力孜,加米拉.吾守尔,吐尔根.依布拉音,阿依佐克拉.瓦依提)
    原始算法在反向遍历时 当遇到两个并列元音（VV）时并不会切分，只当遇到 VC 时进行切分，这样在文本中出现多个外来词时 音节的划分可能会更加准确。
    但在这里默认会切分 两个并列元音（VV） 这样使得，大部分情况下的音节划分可能更加准确
    """

    def __init__(self):
        super().__init__(ProcesClass.ULY, ProcesType.SYLLABLES,'DefaultULYDivideSyllablesProcessor')
        self.syllables_form = ['V', 'VC', 'CV', 'CVC', 'VCC', 'CVCC', 'CCV', 'CCVC', 'CCVCC', 'CVV', 'CVVC',
                               'CCCV']
        self.right_single_quotation_mark = '\u2019'  # (’,\u2019 ) 分割符
        self.Hemze = '\u0626'

    def process(self, text: str, split_vowels: bool = True, delimiter: str = ''):
        """
        划分音节。因为ULY中没有hemze但多了一个 "’"(\u2019 ) 分割符，
        因此需要对UEYDivideSyllablesProcessor中的处理逻辑进行一些修改，具体逻辑如下：
        1. 按照空格进行分割，分割后的子元素叫word。
        2. （给改内容）将word按"’" 进行分割，分割后的子元素叫block。
        3. （新添加）遍历block，如果前一个block的最后一个元素为辅音，且当前block的第一个元素为元音则保留，不然合并（中间添加"’"(\u2019 ) ）。
        4. 从block生成VC二元列表（v_c_list）
        5. 将v_c_list进行反向遍历并划分音节
        6. 正向遍历并纠正音节
        7. 如果音节开头为元音则在前面添加Hemze并生成音节的原始形式（非VC）
        8. 整合并返回

        :param text: 需要处理的文字
        :param split_vowels: 是否切割两个并列元音(VV)。如果文字中包含了太多汉语借词时可以设置成False
        :param delimiter: 词之间的分隔符
        :return: 转换后的音节字符串
        """
        syllable_list = []
        for word in text.split():
            word_syllable_list = []
            for block in self.splitWord(word):
                if not block:
                    continue
                # 元音辅音（vowel consonants）二元列表，v 表示元音，c 表示辅音
                block=self.mk_Letter_List(block)
                v_c_list = []
                for c in block:
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
                    syllable = block[index:index + len(i)]
                    block_syllable_list.append(''.join(syllable))
                    index += len(i)
                word_syllable_list += block_syllable_list
            syllable_list.append(' '.join(word_syllable_list))
        return f' {delimiter} '.join(syllable_list)

    def splitWord(self, word: str) -> list[str]:
        """
        按  "’"(\u2019 ) 分割，并啊不能规则合并
        :param word: 需要分割的一个词（不是句子）
        :return: 分割结果列表
        """
        sub_strs = word.split(self.right_single_quotation_mark)
        index = 1

        while index < len(sub_strs):
            if not is_vowel(sub_strs[index - 1][-1]) and is_vowel(sub_strs[index][0]):
                index += 1
                continue
            else:
                sub_strs[index - 1:index + 1] = [
                    sub_strs[index - 1] + self.right_single_quotation_mark + sub_strs[index]]

        return sub_strs

    def mk_Letter_List(self,word:str) -> list[str]:

        result = []
        word += ' ' + ' '  # 添加两个空格
        prev_char = word[0]
        index = 1
        while len(word) - 1 > index:
            if prev_char + word[index] in ['zh','gh','sh','ng']:
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
    def iterateSyllable(self, block: str) -> list[str] | None:
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
