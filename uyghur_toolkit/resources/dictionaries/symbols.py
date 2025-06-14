# symbol,UEY,ULY,UYY,UKY,IPA
SYMBOLS = [('%', 'پىرسەنت', 'pirsent', 'pirsənt', 'пирсәнт', 'pirsɛnt'),
           ('$', 'دوللار', 'dollar', 'dollar', 'доллар', 'dollɑr'),
           ('€', 'يېۋرو', 'yëwro', 'yewro', 'йевро', 'jewro'),
           ('£', 'فونىستىرلىڭ', 'fonistirling', 'fonistirling', 'фонистирлиң', 'fonistirliŋ'),
           ('¥', 'يۇئەن', 'yu’en', 'yuən', 'йуән', 'juɛn'),
           ('℃', 'سېلسىيە گرادۇس', 'sëlsiye gradu', 'selsiyə gradus', 'селсийә градус', 'selsijɛ ɡrɑdus'),
           ('°', 'گرادۇس', 'gradu', 'gradus', 'градус', 'ɡrɑdus')]

PUNCTUATIONS = [
    (')', '(', '(', '(', '('),
    ('(', ')', ')', ')', ')'),
    (']', '[', '[', '[', ']'),
    ('[', ']', ']', ']', ']'),
    ('}', '{', '{', '{', '}'),
    ('{', '}', '}', '}', '}'),
    ('>', '<', '<', '<', '<'),
    ('<', '>', '>', '>', '>'),
    ('»', '«', '«', '«', '«'),
    ('«', '»', '»', '»', '»'),
    ('؟', '?', '?', '?', '?'),
    ('؛', ';', ';', ';', ';'),
    ('،', ',', ',', ',', ','),
]

def getSymbolMap(v_index:int,reverse:bool=False) -> dict[str, str] | None:
    if v_index > 5:
        return None
    if reverse:
        return {item[v_index]: item[0] for item in SYMBOLS}
    return {item[0]: item[v_index] for item in SYMBOLS}

UEY_SYMBOL_MAP = getSymbolMap(1)
UEY_SYMBOL_MAP_REVERSE = getSymbolMap(1,reverse=True)
ULY_SYMBOL_MAP = getSymbolMap(2)
ULY_SYMBOL_MAP_REVERSE = getSymbolMap(2,reverse=True)
UYY_SYMBOL_MAP = getSymbolMap(3)
UYY_SYMBOL_MAP_REVERSE = getSymbolMap(3,reverse=True)
UKY_SYMBOL_MAP = getSymbolMap(4)
UKY_SYMBOL_MAP_REVERSE = getSymbolMap(4,reverse=True)
IPA_SYMBOL_MAP = getSymbolMap(5)
IPA_SYMBOL_MAP_REVERSE = getSymbolMap(5,reverse=True)
