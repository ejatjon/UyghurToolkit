from uyghur_toolkit.resources.dictionaries.vowels import UEY_VOWELS, UKY_VOWELS, ULY_VOWELS, UYY_VOWELS, IPA_VOWELS


def BIT(n:int):
    return 1 << n

def replace_whitespace(text):
    """
    将多个空格替换成一个空格
    :param text:
    :return:
    """
    text_list = text.split()  # 使用split()函数将字符串按照空格分割成列表
    new_text = ' '.join(text_list)  # 使用join()函数将列表中的元素以单个空格进行连接
    return new_text

