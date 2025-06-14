# number,UEY,ULY,UYY,UKY,IPA
NUMBERS = [(0, 'نۆل', 'nöl', 'nɵl', 'нөл', 'nøl'),
           (1, 'بىر', 'bir', 'bir', 'бир', 'bir'),
           (2, 'ئىككى', 'ikki', 'ikki', 'икки', 'ikki'),
           (3, 'ئۈچ', 'üch', 'üq', 'үч', 'yt͡ʃ'),
           (4, 'تۆت', 'töt', 'tɵt', 'төт', 'tøt'),
           (5, 'بەش', 'besh', 'bəx', 'бәш', 'bɛʃ'),
           (6, 'ئالتە', 'alte', 'altə', 'алтә', 'ɑltɛ'),
           (7, 'يەتتە', 'yette', 'yəttə', 'йәттә', 'jɛttɛ'),
           (8, 'سەككىز', 'sekkiz', 'səkkiz', 'сәккиз', 'sɛkkiz'),
           (9, 'توققۇز', 'toqquz', 'toⱪⱪuz', 'тоққуз', 'toqquz'),
           (10, 'ئون', 'on', 'on', 'он', 'on'),
           (20, 'يىگىرمە', 'yigirme', 'yigirmə', 'йигирмә', 'jiɡirmɛ'),
           (30, 'ئوتتۇز', 'ottuz', 'ottuz', 'оттуз', 'ottuz'),
           (40, 'قىرىق', 'qiriq', 'ⱪiriⱪ', 'қириқ', 'qiriq'),
           (50, 'ئەللىك', 'ellik', 'əllik', 'әллик', 'ɛllik'),
           (60, 'ئاتمىش', 'atmish', 'atmix', 'атмиш', 'ɑtmiʃ'),
           (70, 'يەتمىش', 'yetmish', 'yətmix', 'йәтмиш', 'jɛtmiʃ'),
           (80, 'سەكسەن', 'seksen', 'səksən', 'сәксән', 'sɛksɛn'),
           (90, 'توقسان', 'toqsan', 'toⱪsan', 'тоқсан', 'toqsɑn'),
           (100, 'يۈز', 'yüz', 'yüz', 'йүз', 'jyz'),
           (1000, 'مىڭ', 'ming', 'ming', 'миң', 'miŋ'),
           (1000000, 'مىليون', 'milyon', 'milyon', 'милйон', 'miljon'),
           (1000000000, 'مىليارد', 'milyard', 'milyard', 'милйард', 'miljɑrd'),
           (1000000000000, 'تىرلىيون', 'tirliyon', 'tirliyon', 'тирлийон', 'tirlijon')]

def _getNumberMap(v_index:int,reverse:bool=False) -> dict[int, str] | dict[str, int] | None:
    if v_index >5:
        return None
    if reverse:
        return {item[v_index]: item[0] for item in NUMBERS}
    return {item[0]: item[v_index] for item in NUMBERS}

    
    

UEY_NUMBER_MAP: dict[int, str] = _getNumberMap(1)
UEY_REVERSE_NUMBER_MAP: dict[str, int] = _getNumberMap(1,reverse=True)
ULY_NUMBER_MAP: dict[int, str] = _getNumberMap(2)
ULY_REVERSE_NUMBER_MAP: dict[str, int] = _getNumberMap(2,reverse=True)
UYY_NUMBER_MAP: dict[int, str] = _getNumberMap(3)
UYY_REVERSE_NUMBER_MAP: dict[str, int] = _getNumberMap(3,reverse=True)
UKY_NUMBER_MAP: dict[int, str] = _getNumberMap(4)
UKY_REVERSE_NUMBER_MAP: dict[str, int] = _getNumberMap(4,reverse=True)
IPA_NUMBER_MAP: dict[int, str] = _getNumberMap(5)
IPA_REVERSE_NUMBER_MAP: dict[str, int] = _getNumberMap(5,reverse=True)



