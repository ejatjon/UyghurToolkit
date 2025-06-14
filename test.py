# // +----------------------------------------------------------------------
# // | Update: 2022-12-06 10:24
# // +----------------------------------------------------------------------
# // | Author: Kerindax <1482152356@qq.com>
# // +----------------------------------------------------------------------
# // | Project Url: https://gitee.com/kerindax/UyghurCharUtils
# // +----------------------------------------------------------------------
import re


class UyghurCharUtils(object):
    """description of class"""
    BASIC = 0  # 基本区形式  A
    ALONE = 1  # 单独形式    A
    HEAD = 2  # 头部形式    A_
    CENTR = 3  # 中部形式   _A_
    REAR = 4  # 后部形式   _A
    # 双目字列表，转换扩展区的时候需要替换
    special = [
        {"basic": [0x644, 0x627], "extend": [0xfefc], "link": [0xfee0, 0xfe8e]},  # LA
        {"basic": [0x644, 0x627], "extend": [0xfefb], "link": [0xfedf, 0xfe8e]}  # _LA
    ]
    # 单字母列表
    charCode = {}

    # 数字转换对应的字母
    def fromCharCode(self, number):
        return chr(number)

    def __init__(self, *args, **kwargs):
        # /**
        # * 基本码, 单独形式, 头部形式, 中部形式, 后部形式]
        # * [  A  ,     A   ,    A_   ,   _A_  ,   _A   ]
        # */
        for row in [
            [0x626, 0xfe8b, 0xfe8b, 0xfe8c, 0xfe8c],  # 1 --- 00-Hemze
            [0x627, 0xfe8d, 0xfe8d, 0xfe8e, 0xfe8e],  # 0 --- 01-a
            [0x6d5, 0xfee9, 0xfee9, 0xfeea, 0xfeea],  # 0 --- 02-:e
            [0x628, 0xfe8f, 0xfe91, 0xfe92, 0xfe90],  # 1 --- 03-b
            [0x67e, 0xfb56, 0xfb58, 0xfb59, 0xfb57],  # 1 --- 04-p
            [0x62a, 0xfe95, 0xfe97, 0xfe98, 0xfe96],  # 1 --- 05-t
            [0x62c, 0xfe9d, 0xfe9f, 0xfea0, 0xfe9e],  # 1 --- 06-j
            [0x686, 0xfb7a, 0xfb7c, 0xfb7d, 0xfb7b],  # 1 --- 07-q
            [0x62e, 0xfea5, 0xfea7, 0xfea8, 0xfea6],  # 1 --- 08-h
            [0x62f, 0xfea9, 0xfea9, 0xfeaa, 0xfeaa],  # 0 --- 09-d
            [0x631, 0xfead, 0xfead, 0xfeae, 0xfeae],  # 0 --- 10-r
            [0x632, 0xfeaf, 0xfeaf, 0xfeb0, 0xfeb0],  # 0 --- 11-z
            [0x698, 0xfb8a, 0xfb8a, 0xfb8b, 0xfb8b],  # 0 --- 12-:zh
            [0x633, 0xfeb1, 0xfeb3, 0xfeb4, 0xfeb2],  # 1 --- 13-s
            [0x634, 0xfeb5, 0xfeb7, 0xfeb8, 0xfeb6],  # 1 --- 14-x
            [0x63a, 0xfecd, 0xfecf, 0xfed0, 0xfece],  # 1 --- 15-:gh
            [0x641, 0xfed1, 0xfed3, 0xfed4, 0xfed2],  # 1 --- 16-f
            [0x642, 0xfed5, 0xfed7, 0xfed8, 0xfed6],  # 1 --- 17-:k
            [0x643, 0xfed9, 0xfedb, 0xfedc, 0xfeda],  # 1 --- 18-k
            [0x6af, 0xfb92, 0xfb94, 0xfb95, 0xfb93],  # 1 --- 19-g
            [0x6ad, 0xfbd3, 0xfbd5, 0xfbd6, 0xfbd4],  # 1 --- 20-:ng
            [0x644, 0xfedd, 0xfedf, 0xfee0, 0xfede],  # 1 --- 21-l
            [0x645, 0xfee1, 0xfee3, 0xfee4, 0xfee2],  # 1 --- 22-m
            [0x646, 0xfee5, 0xfee7, 0xfee8, 0xfee6],  # 1 --- 23-n
            [0x6be, 0xfbaa, 0xfbac, 0xfbad, 0xfbab],  # 1 --- 24-:h
            [0x648, 0xfeed, 0xfeed, 0xfeee, 0xfeee],  # 0 --- 25-o
            [0x6c7, 0xfbd7, 0xfbd7, 0xfbd8, 0xfbd8],  # 0 --- 26-u
            [0x6c6, 0xfbd9, 0xfbd9, 0xfbda, 0xfbda],  # 0 --- 27-:o
            [0x6c8, 0xfbdb, 0xfbdb, 0xfbdc, 0xfbdc],  # 0 --- 28-v
            [0x6cb, 0xfbde, 0xfbde, 0xfbdf, 0xfbdf],  # 0 --- 29-w
            [0x6d0, 0xfbe4, 0xfbe6, 0xfbe7, 0xfbe5],  # 1 --- 30-e
            [0x649, 0xfeef, 0xfbe8, 0xfbe9, 0xfef0],  # 1 --- 31-i
            [0x64a, 0xfef1, 0xfef3, 0xfef4, 0xfef2],  # 1 --- 32-y

            [0x6c5, 0xfbe0, 0xfbe0, 0xfbe1, 0xfbe1],  # 0 --- kz o_
            [0x6c9, 0xfbe2, 0xfbe2, 0xfbe3, 0xfbe3],  # 0 --- kz o^
            [0x62d, 0xfea1, 0xfea3, 0xfea4, 0xfea2],  # 1 --- kz h
            [0x639, 0xfec9, 0xfecb, 0xfecc, 0xfeca],  # 1 --- kz c
        ]:
            list = []
            for el in row:
                list.append(self.fromCharCode(el))
            for item in list:
                self.charCode[item] = list
        return super().__init__(*args, **kwargs)

    # /**
    # * 基本区->转换->扩展区
    # * @param source 要转换的内容，可以包含混合字符串
    # * @return 已转换的内容
    # */
    def Basic2Extend(self, source):
        # 转换范围；不包含哈语的0x0621字母,问号,双引号和Unicode区域的符号
        convertRang = r'[\u0622-\u064a\u0675-\u06d5]+'
        # 分割范围，有后尾的字符表达式
        suffixRang = r'[^\u0627\u062F-\u0632\u0648\u0688-\u0699\u06C0-\u06CB\u06D5]'

        def replacefunction(match):
            word = match.group()
            returns = re.sub(suffixRang, lambda m1: m1.group() + '  ', word).strip()
            returns = re.sub(r'(^|\S)(\S)(?=$|\S)', lambda m: m.group(1) + self.getChar(m.group(2), self.ALONE),
                             returns)
            returns = re.sub(r'(\S|^)(\S)\s', lambda m: m.group(1) + self.getChar(m.group(2), self.HEAD), returns)
            returns = re.sub(r'\s(\S)\s', lambda m: self.getChar(m.group(1), self.CENTR), returns)
            returns = re.sub(r'\s(\S)(?=\S|$)', lambda m: self.getChar(m.group(1), self.REAR), returns)
            return self.extendLa(returns)

        return re.sub(convertRang, replacefunction, source)

    # /**
    # * 扩展区   转换   基本区
    # * @param source 要转换的内容
    # * @return 已转换的内容
    # */
    def Extend2Basic(self, source):
        # 扩展区范围；FB50-FDFF ->区域A    FE70-FEFF -> 区域B
        extendRang = r'[\ufb50-\ufdff\ufe70-\ufeff]'
        return re.sub(extendRang, lambda m: self.getChar(m.group(), self.BASIC), self.basicLa(source))

    # /**
    # * 基本区  转换   反向扩展区
    # * @param source 要转换的内容
    # * @return 已转换的内容
    # */
    def Basic2RExtend(self, source):
        return self.reverseAscii(self.reverseSubject(self.Basic2Extend(source)));

    # /**
    # * 反顺序扩展区   转换   基本区
    # * @param source 要转换的内容
    # * @return 已转换的内容
    # */
    def RExtend2Basic(self, source):
        return self.Extend2Basic(self.reverseSubject(self.reverseAscii(source)));

    # /**
    # * 音节索引
    # */
    def BasicSyllable(self, source):
        # 音节切开专用，取韵母
        finalsRang = r'([\u0627\u06d5\u0648\u06c7\u06c6\u06c8\u06d0\u0649\u06c9\u06c5])([^\u0627\u06d5\u0648\u06c7\u06c6\u06c8\u06d0\u0649\u06c9\u06c5]+)(?=[\u0627\u06d5\u0648\u06c7\u06c6\u06c8\u06d0\u0649\u06c9\u06c5])'

        def replacefunction(match):
            word = match.group()

            def finalsRangfunction(m):
                ch2 = m.group(2)
                index = int(len(ch2) / 2)
                return m.group(1) + ch2[:index] + ' ' + ch2[index:]

            return re.sub(finalsRang, finalsRangfunction, word)

        return re.sub(r'[^\s]+', replacefunction, source)

    # /**
    # * Ascii区反转
    # */
    def reverseAscii(self, source):
        # 特助转换区，扩展区反向转换的时候需要替换
        symbolRang = r'[}{><»«\)\(\[\]]'
        symbolList = {
            ')': '(',
            '(': ')',
            ']': '[',
            '[': ']',
            '}': '{',
            '{': '}',
            '>': '<',
            '<': '>',
            '»': '«',
            '«': '»',
        }
        # 不包含扩展区中部包含空格字符集；FB50-FDFF ->区域A    FE70-FEFF -> 区域B
        notExtendRang = r'[^\ufb50-\ufdff\ufe70-\ufeff\s]+(\s[^\ufb50-\ufdff\ufe70-\ufeff\s]+)*'

        def replacefunction(match):
            array = list(match.group())
            array.reverse()
            return re.sub(notExtendRang,
                          lambda m: symbolList.get(m.group()) if symbolList.get(m.group()) else m.group(),
                          ''.join(array))

        return re.sub(notExtendRang, replacefunction, source)

    # /**
    # * 对象反转
    # */
    def reverseSubject(self, str):
        def replacefunction(match):
            array = list(match.group())
            array.reverse()
            return ''.join(array)

        return re.sub(r'.+', replacefunction, str)

    # /**
    # * 获取对应字母
    # */
    def getChar(self, ch, index):
        return self.charCode.get(ch)[index] if self.charCode.get(ch) else ch

    # /**
    # * La字母转换扩展区
    # */
    def extendLa(self, source):
        for item in self.special:
            source = source.replace(self.getString(item['link']), self.getString(item['extend']))
        return source

    # /**
    # * La字母转换基本区
    # */
    def basicLa(self, source):
        for item in self.special:
            source = source.replace(self.getString(item['extend']), self.getString(item['basic']))
        return source

    # /**
    # * 双目字母转换字符串
    # */
    def getString(self, value):
        return ''.join(self.fromCharCode(el) for el in value)



utils  = UyghurCharUtils()
source = "خەلىقئارا"

target1 = utils.Basic2Extend(source) #基本区 转换 扩展区
target2 = utils.Extend2Basic(target1) #扩展区 转换 基本区

target3 = utils.Basic2RExtend(source) #基本区 转换 反向扩展区
target4 = utils.RExtend2Basic(target3) #反向扩展区 转换 基本区

target5 = utils.BasicSyllable(source) #音节索引

print(target1)
print(target2)
print(target3)
print(target4)
print(target5)

