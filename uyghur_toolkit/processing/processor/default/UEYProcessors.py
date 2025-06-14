import re

from uyghur_toolkit.processing.ProcesClass import ProcesClass
from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.processor.Processor import Processor
from uyghur_toolkit.resources.dictionaries.letter_mapping.SPECIAL_UEY_LATTER import normalize_La, normalize_Hemze
from uyghur_toolkit.resources.dictionaries.letter_mapping.UEY_SCRIPTS import UEY_SCRIPTS
from uyghur_toolkit.resources.dictionaries.numbers import UEY_NUMBER_MAP, UEY_REVERSE_NUMBER_MAP
from uyghur_toolkit.resources.dictionaries.symbols import PUNCTUATIONS, UEY_SYMBOL_MAP
from uyghur_toolkit.resources.dictionaries.uey_to_base import UEY_TO_BASE
from uyghur_toolkit.resources.dictionaries.vowels import UEY_VOWELS
from uyghur_toolkit.utils.number_tools import decompose_number, decimal_number, decimal_places, divide, toDecimal


def is_vowel(s: str) -> bool:
    if s in UEY_VOWELS:
        return True
    return False


def int_to_uey(num: int) -> str:
    """
    将整数转换为UEY数字表示
    :param num: 整数
    :return: UEY数字表示的字符串
    """
    if num == 0:
        return UEY_NUMBER_MAP[0]
    components = decompose_number(num)
    result = []
    for unit, count in components:
        if unit == 1:  # 个位处理
            result.append(UEY_NUMBER_MAP[count])
        elif unit == 10:  # 十位处理（如20、30等）
            result.append(UEY_NUMBER_MAP[unit * count])
        else:  # 其他单位处理
            count_str = int_to_uey(count)
            result.append(f"{count_str} {UEY_NUMBER_MAP[unit]}")
    return " ".join(result)


def float_to_uey(num: float) -> str:
    """
    将浮点数转换为Uyghur数字表示
    :param num: 浮点数
    :return: Uyghur数字表示的浮点数字符串
    """
    integer_part = int_to_uey(int(num))
    decimal_part = int_to_uey(decimal_number(num))
    if decimal_part == '0':
        return integer_part
    decimal_places_count = decimal_places(num)
    decimal_places_unit = UEY_NUMBER_MAP.get(10 ** decimal_places_count, int_to_uey(10 ** decimal_places_count))

    return f"{integer_part} پۈتۈن {decimal_places_unit} دە {decimal_part}"


def number_hyphen_converter(s: str) -> str:
    """
    替换数字前的中划线（-），text是一个维语表示的数，此函数会给他添加 ىنچى 后缀
    :param s: 是一个维语表示的数
    :return: 替换后的字符串
    """
    s = list(s)
    if s[-1] == '\u06d5':  # ە
        s = s[:-1] + ['\u0649', '\u0646', '\u0686', '\u0649']  # ىنچى
    elif s[-1] == '\u0649':  # ى
        s = s[:-1] + ['\u0649', '\u0646', '\u0686', '\u0649']  # نچى
    else:
        s += ['\u0649', '\u0646', '\u0686', '\u0649']  # ىنچى
    return ''.join(s)


def number_hyphen_reverse(text: str):
    regex = re.compile(fr'''
    (\S+?)# 匹配非空字符（非贪婪）
    ({re.escape(''.join(['\u0649', '\u0646', '\u0686', '\u0649']))}) # 后缀 ىنچى
    (?=\s|$) # 后边界检查（空格或结尾）
    ''', flags=re.VERBOSE | re.UNICODE | re.DOTALL)

    # 定义替换函数
    def replacement(match):
        prefix = match.group(1)
        if prefix in UEY_REVERSE_NUMBER_MAP.keys():
            return ' ' + prefix + ' - '
        elif prefix + '\u0649' in UEY_REVERSE_NUMBER_MAP.keys():  # + 'ى'
            return ' ' + prefix + '\u0649' + ' - '
        elif prefix + '\u06d5' in UEY_REVERSE_NUMBER_MAP.keys():  # + 'ە'
            return ' ' + prefix + '\u06d5' + ' - '
        else:
            return match.group(0)  # 默认不替换

    return regex.sub(replacement, text)

def get_uey_forms(c: str, autofill: bool = True) -> dict[str, str] | dict[str, str] | None:
    """
    获取字母形态信息。如果autofill为真，则会按照一定的优先级进行自动填充
    :param autofill: 自动填充缺失的字母形式
    :param c: UEY 字母的基本形式
    :return: 字母形态信息
    """

    def get_form(f: dict[str, dict[str, str]]) -> dict[str, str] | None:
        if autofill:
            base = f['UEY']['Base']
            isolated = f['UEY']['Isolated']
            if isolated == '':
                isolated = base
            simple_isolated = f['UEY']['Simple Isolated']
            if simple_isolated == '':
                simple_isolated = isolated
            initial = f['UEY']['Initial']
            if initial == '':
                initial = simple_isolated
            simple_initial = f['UEY']['Simple Initial']
            if simple_initial == '':
                simple_initial = initial
            final = f['UEY']['Final']
            if final == '':
                final = simple_isolated
            separated_final = f['UEY']['Separated Final']
            if separated_final == '':
                separated_final = final
            medial = f['UEY']['Medial']
            if medial == '':
                medial = final
            medial_simple = f['UEY']['Separated Medial']
            if medial_simple == '':
                medial_simple = separated_final
            return {
                'Base': base,
                'Isolated': isolated,
                'Simple Isolated': simple_isolated,
                'Initial': initial,
                'Simple Initial': simple_initial,
                'Medial': medial,
                'Separated Medial': medial_simple,
                'Final': final,
                'Separated Final': separated_final
            }
        form = {}
        for k, v in f['UEY'].items():
            if v == '':
                continue
            form[k] = v
        return form if form else None

    if c == '\u0626':
        if autofill:
            return {
                'Base': '\u0626',  # ئ
                'Isolated': '\u0626',  # ئ
                'Simple Isolated': '\u0626',
                'Initial': '\uFE8B',  # ﺋ
                'Simple Initial': '\uFE8B',
                'Medial': '\uFE8C',  # ﺌ
                'Separated Medial': '\uFE8C',
                'Final': '\u0626',
                'Separated Final': '\u0626'
            }
        return {
            'Base': '\u0626',  # ئ
            'Isolated': '\u0626',  # ئ
            'Initial': '\uFE8B',  # ﺋ
            'Medial': '\uFE8C',  # ﺌ
        }
    forms = UEY_SCRIPTS.get(c, None)
    if forms:
        return get_form(forms)
    return None


def uey_to_base(s: str) -> str:
    """
    吧 UEY 字符转换成基本形式
    :param s: 要转换的字符串
    :return: 转换后的字符串
    """
    s = normalize_La(s)
    s = normalize_Hemze(s)
    return ''.join([UEY_TO_BASE.get(c, c) for c in s])


def uey_punctuation_to_other(s: str, target: int) -> str:
    """
    将UEY标点符号转换成ULY,UYY,UKY,IPA 的标点符号
    :param s: 要转换的字符串
    :param target: 目标标点符号类型，值应为 1,2,3,4 (表示 ULY,UYY,UKY,IPA) 中的一个
    :return: 处理结果
    """
    if target not in [1, 2, 3, 4]:
        raise ValueError("Invalid target punctuation type")
    for punctuation in PUNCTUATIONS:
        s = s.replace(punctuation[0], punctuation[target])
    return s


class UEYNumberProcessor(Processor):
    def __init__(self, exclude_before: list[str] = None, exclude_after: list[str] = None, add_space: bool = True):
        """
        初始化参数
        :param exclude_before: 数字前缀，有此前缀的数字将被忽略
        :param exclude_after: 数字后缀，有此后缀的数字将被忽略
        :param add_space: 是否在匹配到的数字前后添加空格
        """
        super().__init__(ProcesClass.UEY, ProcesType.NUMBER,'DefaultUEYNumberProcessor')
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
        将文本中的阿拉伯整数转换成 Uyghur(维吾尔语) 表示
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
            number = int_to_uey(int(number_str))

            prefix, suffix = self._format_spaces(prefix, suffix)

            return f"{prefix}{number}{suffix}"

        return regex.sub(replace, text)

    def FloatNumber(self, text: str) -> str:
        """
        将文本中的阿拉伯小数转换成 Uyghur(维吾尔语) 表示
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
            number = float_to_uey(float(number_str))

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


class UEYNumberReverseProcessor(Processor):
    """
    吧Uyghur 数字转换成阿拉伯数字会有点复杂，以下是详细的处理逻辑(注意 如果出现 以空格分割的数将会出现问题)
    1. 吧Uyghur数字转换成 (数字（int），不是数量级(bool)) 格式的列表，下面称为pending（暂存数字）
    例如：بىر يۈز يىگىرمە ئۈچ مىڭ توققۇز يۈز ئەللىك بەش(123955) -> [(1, True), (100, False), (20, True), (3, True), (1000, False), (9, True), (100, False), (50, True), (5, True)]
    2. pending分成几个数量级单调递增的部分
    这里说的数量级说的是为维语中表示数量级的数(维语中的万不常用因此没包含在里面) 如 百 100 千1000 百万100000 ...
    例如：[(1, True), (100, False), (20, True), (3, True), (1000, False), (9, True), (100, False), (50, True), (5, True)]
    -> [
        [(1, True), (100, False), (20, True), (3, True), (1000, False)],
        [(9, True), (100, False)], [(50, True)],
        [(5, True)]
       ]
    每个部分的数量级都是单调递增的 (100 < 1000 )
    3. 然后吧每个单调递增的数字列表整合成 阿拉伯数
    整合的规则是： p/c -> p: 加法
                p/c -> c: 乘法
    其中 p 表示 非数量级数  c 表示 数量级数   / 表示 或   (这个规则是我自己观察出来的，经过测试没发现问题)
    例如：[(1, True), (100, False), (20, True), (3, True), (1000, False)]
    第一步 1 和 100  1 是 p ，100 是 c 。通过规则 p->c 为乘法 结果为c 1*100=100
    第二步 100（第一步结果，类型为c） 和 20 ，通过规则c->p 为加法 结果为p 20+100=120
    第三步 120（第二步结果，类型为p） 和 3  ，通过规则p->p 为加法 结果为p 120+3=123
    第四步 123（第三步结果，类型为p） 和 1000  ，通过规则p->c 为乘法 结果为c 123*1000=123000
    返回123000
    4. 吧各部分整合的结果求和
    例如：sum([123000,950,5])=123955
    """

    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.REVERSE | ProcesType.NUMBER,'DefaultUEYNumberReverseProcessor')

    def process(self, text):
        text = self.reverse_float(text)
        return self.reverse_integer(text)

    def reverse_float(self, text: str):
        """
        将Uyghur 的小数转换成浮点数
        :param text: 转换的文本
        :return: 转换结果
        """
        prefix_str = 'پۈتۈن'
        suffix_str = 'دە'
        result = []  # 结果
        pending_integer = []
        pending_decimal = []
        pending_order = []
        tokens = text.split()
        prefix, suffix = False, False
        for word in tokens:
            if word in UEY_REVERSE_NUMBER_MAP:
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
            if word in UEY_REVERSE_NUMBER_MAP:
                pending.append((UEY_REVERSE_NUMBER_MAP[word], UEY_REVERSE_NUMBER_MAP[word] < 100))
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


class UEYDateProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.DATE,'DefaultUEYDateProcessor')
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
            year_unit = '\u064a\u0649\u0644\u0649'  # يىلى
            month_unit = '\u0626\u0627\u064a\u0646\u0649\u06ad'  # ئايىڭ
            day_unit = '\u0643\u06c8\u0646\u0649'  # كۈنى
            return f"{self.convert_date_number(year)} {year_unit} {self.convert_date_number(month)} {month_unit} {self.convert_date_number(day)} {day_unit}"

        return self.mk_regex().sub(replace_handler, s)

    @staticmethod
    def convert_date_number(s):
        number = int(s)
        uey_number = int_to_uey(number)
        return number_hyphen_converter(uey_number)

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


class UEYDateAndNumberReverseProcessor(Processor):

    def __init__(self):
        super().__init__(ProcesClass.UEY,
                         ProcesType.REVERSE | ProcesType.DATE | ProcesType.NUMBER,'DefaultUEYDateAndNumberReverseProcessor')
        self.number_reverse = UEYNumberReverseProcessor()

    def process(self, text: str, separators: str = '-'):
        regex = re.compile(fr'''
                (\d+)(\s*-\s* {re.escape(''.join(['\u064a', '\u0649', '\u0644', '\u0649']))} \s*)(\d+)(\s*-\s* {re.escape(''.join(['\u0626', '\u0627', '\u064a', '\u0646', '\u0649', '\u06ad']))} \s*)(\d+)(\s*-\s* {re.escape(''.join(['\u0643', '\u06c8', '\u0646', '\u0649']))} \s*)        # year month day        
                ''', flags=re.VERBOSE | re.UNICODE | re.DOTALL)

        def replacement(match):
            year_num = match.group(1)
            month_num = match.group(3)
            day_num = match.group(5)
            return f" {year_num} {separators} {month_num} {separators} {day_num} "

        text = number_hyphen_reverse(text)
        text = self.number_reverse.process(text)
        return regex.sub(replacement, text)


class UEYNormalizeProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.NORMALIZATION,'DefaultUEYNormalizeProcessor')

    def process(self, text):
        return uey_to_base(text)


class UEYNormalizeReverseProcessor(Processor):

    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.REVERSE | ProcesType.NORMALIZATION,'DefaultUEYNormalizeReverseProcessor')

    def process(self, text: str) -> str:
        """
        将标准化的字符串，恢复成原始书写形式
        :param text:
        :return:
        """
        words = text.split()
        result = []
        for word in words:
            result.append(self.reverseWord(word))
        return ' '.join(result)

    @staticmethod
    def getIsolated(c: str) -> str:
        """
        返回独立式字母形式（如果不存在返回基本形式，具体看get_uey_forms）
        :param c: 需要返回的字母的基本形式
        :return: 返回结果
        """
        forms = get_uey_forms(c)
        if not forms:
            return c
        return forms.get('Isolated', '')

    @staticmethod
    def getSimpleIsolated(c: str) -> str:
        """
        返回简单独立式字母形式（如果不存在返回独立式，具体看get_uey_forms）
        :param c: 需要返回的字母的基本形式
        :return: 返回结果
        """
        forms = get_uey_forms(c)
        if not forms:
            return c
        return forms.get('Simple Isolated', '')

    @staticmethod
    def getInitial(c: str) -> str:
        """
        返回后连式字母形式（如果组存在返回简单独立式，具体看get_uey_forms）
        :param c: 需要返回的字母的基本形式
        :return: 返回结果
        """
        forms = get_uey_forms(c)
        if not forms:
            return c
        return forms.get('Initial', '')

    @staticmethod
    def getSimpleInitial(c: str) -> str:
        """
        返回简单后连式字母形式（如果不存在返回后连式，具体看get_uey_forms）
        :param c: 需要返回的字母的基本形式
        :return: 返回结果
        """
        forms = get_uey_forms(c)
        if not forms:
            return c
        return forms.get('Simple Initial', '')

    @staticmethod
    def getMedial(c: str) -> str:
        """
        返回双连式字母形式（如果不存在返回前连式，具体看get_uey_forms）
        :param c: 需要返回的字母的基本形式
        :return: 返回结果
        """
        forms = get_uey_forms(c)
        if not forms:
            return c
        return forms.get('Medial', '')

    @staticmethod
    def getFinal(c: str) -> str:
        """
        返回前连式字母形式（如果不存在返回独立式，具体看get_uey_forms）
        :param c: 需要返回的字母的基本形式
        :return: 返回结果
        """
        forms = get_uey_forms(c)
        if not forms:
            return c
        return forms.get('Final', '')

    def integrateLetter(self, l: list[str]) -> str:
        """
        判断当前字母应该的形式并返回。
        判断逻辑我自己通过观察和经验得出，逻辑简单可能会有错误。以下是具体规则：
        1. 前后为空。当前字母使用使用独立式
        2. 前为空，后不为空。当前字母使用后连式，如果不存在使用简单独立式，也不存在使用独立式
        3. 前不为空，后为空且前一个字母具有双连式或后连式形式。当前字母使用前连式 否则 使用简单独立式（不存在使用独立式）
        4. 前后都不为空且前一个字母具有双连式或后连式形式。当前字母使用双连式，否则使用后连式（诺不存在参考 2 ）
        :param l: 一个长度为4的字母列表 【上上一个字母，上一个字母，当前字母，下一个字母】
        :return: 当前字母应该的书写形式（字母）
        """
        prev_letter = l[1].strip()
        letter = l[2].strip()
        next_letter = l[3].strip()

        if prev_letter == '' and next_letter == '':
            return self.getIsolated(letter)
        elif prev_letter == '' and next_letter != '':
            if self.have_initial(letter):
                return self.getInitial(letter)
            else:
                return self.getSimpleIsolated(letter)
        elif prev_letter != '' and next_letter == '':
            if self.have_medial(prev_letter) or self.have_initial(prev_letter):
                return self.getFinal(letter)
            else:
                return self.getSimpleIsolated(letter)
        else:  # prev_letter != '' and next_letter != ''
            if self.have_medial(prev_letter) or self.have_initial(prev_letter):
                return self.getMedial(letter)
            else:
                return self.getInitial(letter)

    def reverseWord(self, word: str) -> str:
        """
        把一个词，从标准化恢复到书写形式
        :param word: 需要恢复的词
        :return: 恢复结果
        """
        if len(word) <= 1:
            return self.getIsolated(word)
        word = ['', ''] + list(word) + ['']
        result = []
        for i in range(2, len(word) - 1):
            result.append(self.integrateLetter(word[i - 2:i + 2]))
        return ''.join(result)

    @staticmethod
    def is_single_form_consonant(c: str) -> bool:
        """
        判断只有两种书写形式的辅音字母
        :param c: UEY 字母的基本形式
        :return: bool 值，为True表示这个字母只有两个书写形式
        """
        return c in ['\u062f', '\u0631', '\u0632', '\u0698', '\u06cb']  # د,ر,ز,ژ,ۋ

    @staticmethod
    def have_initial(c: str) -> bool:
        """
        判断具有后连式(Initial)的字母
        :param c: UEY 字母的基本形式
        :return: bool 值，为True表示这个字母具有后连式形式
        """
        forms = get_uey_forms(c, autofill=False)
        if not forms:
            return False
        a = True if forms.get('Initial', None) else False
        return True if forms.get('Initial', None) else False

    @staticmethod
    def have_medial(c: str) -> bool:
        """
        判断具有双连式(Medial)的字母
        :param c: UEY 字母的基本形式
        :return: bool 值，为True表示这个字母具有双连式形式
        """
        forms = get_uey_forms(c, autofill=False)
        if not forms:
            return False
        return True if forms.get('Medial', None) else False

    @staticmethod
    def have_final(c: str) -> bool:
        """
        判断具有前连式(Final)的字母
        :param c: UEY 字母的基本形式
        :return: bool 值，为True表示这个字母具有前连式形式
        """
        forms = get_uey_forms(c, autofill=False)
        if not forms:
            return False
        return True if forms.get('Final', None) else False


class UEYSymbolsProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.SYMBOL,'DefaultUEYSymbolsProcessor')

    def process(self, text: str) -> str:
        for k, v in UEY_SYMBOL_MAP.items():
            text = text.replace(k, v)
        return text


class UEYSymbolsReverseProcessor(Processor):
    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.SYMBOL | ProcesType.REVERSE,'DefaultUEYSymbolsReverseProcessor')

    def process(self, text: str) -> str:
        for k, v in UEY_SYMBOL_MAP.items():
            text = text.replace(v, k)
        return text


class UEYToIPAProcessor(Processor):
    """
    UEY 转换到 IPA
    """

    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.TO_IPA,'DefaultUEYToIPAProcessor')
        self.hemze = "\u0626"

    def process(self, text: str) -> str:
        """
        将UEY字符串转换成，IPA字符串（如果一个字符对应多个IPA字符，则只是用第一个）。
        :param text: 要转换的字符串
        :return: 处理结果
        """
        text = uey_to_base(text)
        result = []
        for c in text:
            if c == self.hemze:
                continue
            forms = UEY_SCRIPTS.get(c, None)
            if forms:
                result.append(forms['IPA'][0])
            else:
                result.append(c)
        return uey_punctuation_to_other(''.join(result), 4)


class UEYToUKYProcessor(Processor):
    """
    UEY 转换到 UKY
    西里尔维语除了32个字母以外还多出了其他的字母（ы、ё、ц、э、ю、я...），
    主要用于俄语外来词.其中我们只处理 ю、я
    """

    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.TO_UKY,'DefaultUEYToUKYProcessor')
        self.hemze = "\u0626"

    def process(self, text: str) -> str:
        """
        将UEY字符串转换成UKY字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = uey_to_base(text)
        result = []
        for c in text:
            if c == self.hemze:
                continue
            forms = UEY_SCRIPTS.get(c, None)
            if forms:
                result.append(forms['UKY']['other'])
            else:
                result.append(c)

        return (uey_punctuation_to_other(''.join(result), 3)
                .replace('й‍‍у', '\u044e')
                .replace('йa', '\u044f'))  # 处理 ю、я


class UEYToULYProcessor(Processor):
    """
    UEY 转换到 ULY,
    UEY字母 ئ 在拉丁维文中没有对应字符。但拉丁维文中也有分隔符（撇号，’ == /u2019）：
    1. 词中音节如果以元音开始，而前一个音节以辅音结束，在该元音前加撇号分隔。如前一个音节以元音结束，不加撇号.
    2. 在词中如果 gh、ng、sh、zh 并不代表双字母单辅音，使用分隔号分隔。
    """

    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.TO_ULY,'DefaultUEYToULYProcessor')
        self.divide_syllables = UEYDivideSyllablesProcessor()
        self.hemze = '\u0626'
        self.right_single_quotation_mark = '\u2019'  # (’,\u2019 ) 分割符

    def process(self, text: str) -> str:
        text = uey_to_base(text)
        result = []
        for word in text.split():
            result.append(self.convertToULY(word))
        return uey_punctuation_to_other(' '.join(result), 1)

    def convertToULY(self, word: str, split_vowels: bool = True):
        word = self.divide_syllables.process(word, split_vowels).replace(self.hemze, '')
        syllables = []
        prev_syllable = ''
        for i in word.split():
            if not prev_syllable:
                prev_syllable = i
                syllables.append(i)
                continue
            if is_vowel(i[0]) and is_vowel(prev_syllable[-1]):
                syllables.append(self.right_single_quotation_mark + i)
            else:
                syllables.append(i)
            prev_syllable = i
        uly_word = ''
        for s in syllables:

            for c in s:
                if not uly_word:
                    uly_word = self.getULYChar(c)
                    continue
                c = self.getULYChar(c)
                if uly_word[-1] + c[0] in ['gh', 'ng', 'sh', 'zh']:  # ULY 没有字母c 因此ch 不会产生歧义
                    uly_word += self.right_single_quotation_mark + c
                else:
                    uly_word += c
        return uly_word

    def getULYChar(self, c: str) -> str:
        forms = UEY_SCRIPTS.get(c, None)
        if forms:
            return forms['ULY']['other']
        else:
            return c


class UEYToUYYProcessor(Processor):
    """
    UEY 转换到 UYY
    """

    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.TO_UYY,'DefaultUEYToUYYProcessor')
        self.hemze = "\u0626"

    def process(self, text: str) -> str:
        """
        将UEY字符串转换成UYY字符串。
        :param text: 要转换的文本
        :return: 处理结果
        """
        text = uey_to_base(text)
        result = []
        for c in text:
            if c == self.hemze:
                continue
            forms = UEY_SCRIPTS.get(c, None)
            if forms:
                result.append(forms['UYY']['other'])
            else:
                result.append(c)
        return uey_punctuation_to_other(''.join(result), 2)


class UEYDivideSyllablesProcessor(Processor):
    """
    UEY 音节划分
    具体逻辑参考了论文《现代维吾尔文音节自动切分方法及其实现》(瓦依提.阿不力孜,加米拉.吾守尔,吐尔根.依布拉音,阿依佐克拉.瓦依提)
    原始算法在反向遍历时 当遇到两个并列元音（VV）时并不会切分，只当遇到 VC 时进行切分，这样在文本中出现多个外来词时 音节的划分可能会更加准确。
    但在这里默认会切分 两个并列元音（VV） 这样使得，大部分情况下的音节划分可能更加准确
    """

    def __init__(self):
        super().__init__(ProcesClass.UEY, ProcesType.SYLLABLES,'DefaultUEYDivideSyllablesProcessor')
        self.Hemze = '\u0626'
        self.syllables_form = ['V', 'VC', 'CV', 'CVC', 'VCC', 'CVCC', 'CCV', 'CCVC', 'CCVCC', 'CVV', 'CVVC', 'CCCV']

    def process(self, text: str, split_vowels: bool = True, delimiter: str = ''):
        """
        划分音节。具体逻辑
        1. 按照空格进行分割，分割后的子元素叫word。
        2. 将word按Hemze 进行分割，分割后的子元素叫block。
        3. 从block生成VC二元列表（v_c_list）
        4. 将v_c_list进行反向遍历并划分音节
        5. 正向遍历并纠正音节
        6. 如果音节开头为元音则在前面添加Hemze并生成音节的原始形式（非VC）
        7. 整合并返回
        :param text: 需要处理的文字
        :param split_vowels: 是否切割两个并列元音(VV)。如果文字中包含了太多汉语借词时可以设置成False
        :param delimiter: 词之间的分隔符
        :return: 转换后的音节字符串
        """
        syllable_list = []
        for word in text.split():
            word_syllable_list = []
            for block in self.splitByHemze(word):
                if not block:
                    continue
                # 元音辅音（vowel consonants）二元列表，v 表示元音，c 表示辅音
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
                    if is_vowel(syllable[0]):
                        syllable = self.Hemze + syllable
                    block_syllable_list.append(syllable)
                    index += len(i)
                word_syllable_list += block_syllable_list
            syllable_list.append(' '.join(word_syllable_list))
        return f' {delimiter} '.join(syllable_list)

    def splitByHemze(self, word: str) -> list[str]:
        """
        按 Hemze 分割
        :param word: 需要分割的一个词（不是句子）
        :return: 分割结果列表
        """
        return word.split(self.Hemze)

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
        # 此时已经能处理大部分的音节了。
        # result=[]
        # index=0
        # for i in syllable_list[::-1]:
        #     result.append(block[index:index+len(i)])
        #     index+=len(i)
        #     return result
        # 但是处理一些外来词的音节时会出现问题
        return syllable_list[::-1]

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



