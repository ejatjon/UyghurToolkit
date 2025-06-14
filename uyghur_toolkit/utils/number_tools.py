from decimal import Decimal, getcontext

# 设置全局精度
getcontext().prec = 10

# 单位顺序表（从大到小排列）
UNITS_ORDER = [
    1000000000000,1000000000,1000000, 1000, 100, 10, 1
]

def decompose_number(num:int):
    """
    分解数字到维语数量单位
    示例：314 → 300 + 10 + 4 → [(100,3),(10,1),(1,4)]
    """
    components = []
    for unit in UNITS_ORDER:
       if num >= unit:
            count = num // unit
            components.append((unit, count))
            num -= count * unit
            if num == 0:
                break
    return components

def decimal_places(number:  float|int):
    """
    返回数字有效的小数位数
    示例：3.012300 -> 4
    """
    number=Decimal(number)
    places = 0
    while number != int(number):
        number *= 10
        places += 1
    return places


def integer_number(number: float|int):
    """
    返回数字的有效整数部分
    示例：3.012300 -> 3
    """
    return int(number)

def decimal(number: float|int):
    """
    返回数字的有效小数部分
    示例：3.012300 -> 0.012300
    """
    return Decimal(number) - Decimal(integer_number(number))

def decimal_number(number: float|int):
    """
    返回数字的有效小数部分的数字值
    示例：3.012300 -> 123
    """
    places = decimal_places(number)
    if places == 0:
        return 0
    return int(decimal(number) * (10 ** places))

def divide(a: float|int, b: float|int) -> Decimal:
    a=Decimal(a)
    b=Decimal(b)
    return a / b

def toDecimal(number: float|int) -> Decimal:
    return Decimal(number)

