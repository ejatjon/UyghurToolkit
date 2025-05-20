#  老维文UEY符号ئ（\u0626） 拉丁ULY(’) 不存在UYY,UKY,IPA 的对应表示

IPA_SCRIPTS = {
    '/ɑ/': {
        'ULY': {'sentence_start': 'A', 'other': 'a'},
        'UYY': {'sentence_start': 'A', 'other': 'a'},
        'UEY': {
            'Base': 'ا', #U+0x0627
            'Isolated': 'ئا',
            'Simple Isolated': 'ﺍ', # U+0xFE8D
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﺎ', # U+0xFE8E
            'Separated Final': 'ﺌﺎ' # U+0xFE8E(ﺎ) + \uFE8C(ﺌ)  其他类推
        },
        'UKY': {'sentence_start': 'A', 'other': 'a'}
    },
    '/ɛ/': {
        'ULY': {'sentence_start': 'E', 'other': 'e'},
        'UYY': {'sentence_start': 'Ə', 'other': 'ə'},
        'UEY': {
            'Base': 'ە', #U+0x06D5
            'Isolated': 'ئە',
            'Simple Isolated': 'ﻩ', # U+0xFEE9
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﻪ', # U+0xFEEA
            'Separated Final': 'ﺌﻪ'},
        'UKY': {'sentence_start': 'Ә', 'other': 'ә'}
    },
    '/æ/': {
        'ULY': {'sentence_start': 'E', 'other': 'e'},
        'UYY': {'sentence_start': 'Ə', 'other': 'ə'},
        'UEY': {
            'Base': 'ە', #U+0x06D5
            'Isolated': 'ئە',
            'Simple Isolated': 'ﻩ', # U+0xFEE9
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﻪ', # U+0xFEEA
            'Separated Final': 'ﺌﻪ'},
        'UKY': {'sentence_start': 'Ә', 'other': 'ә'}
    },
    '/o/': {
        'ULY': {'sentence_start': 'O', 'other': 'o'},
        'UYY': {'sentence_start': 'O', 'other': 'o'},
        'UEY': {
            'Base': 'و', # U+0x0648
            'Isolated': 'ئو',
            'Simple Isolated': 'ﻭ', # U+0xFEED
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﻮ', # U+0xFEEE
            'Separated Final': 'ﺌﻮ'},
        'UKY': {'sentence_start': 'О', 'other': 'о'}
    },
    '/u/': {
        'ULY': {'sentence_start': 'U', 'other': 'u'},
        'UYY': {'sentence_start': 'U', 'other': 'u'},
        'UEY': {
            'Base': 'ۇ', # U+0x06C7
            'Isolated': 'ئۇ',
            'Simple Isolated': 'ﯗ', # U+0xFBD7
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﯘ', # U+0xFBD8
            'Separated Final': 'ﺌﯘ'},
        'UKY': {'sentence_start': 'У', 'other': 'у'}
    },
    '/ø/': {
        'ULY': {'sentence_start': 'Ö', 'other': 'ö'},
        'UYY': {'sentence_start': 'Ɵ', 'other': 'ɵ'},
        'UEY': {
            'Base': 'ۆ', # U+0x06C6
            'Isolated': 'ئۆ',
            'Simple Isolated': 'ﯙ', # U+0xFBD9
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﯚ', # U+0xFBDA
            'Separated Final': ''}, #(ﺌﯚ) 维语没有这种用法的词
        'UKY': {'sentence_start': 'Ө', 'other': 'ө'}
    },
    '/y/': {
        'ULY': {'sentence_start': 'Ü', 'other': 'ü'},
        'UYY': {'sentence_start': 'Ü', 'other': 'Ü'},
        'UEY': {
            'Base': 'ۈ', # U+0x06C8
            'Isolated': 'ئۈ',
            'Simple Isolated': 'ﯛ', # U+0xFBDB
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﯜ', # U+0xFBDC
            'Separated Final': ''}, # (ﺌﯜ) 没有这种用法的词
        'UKY': {'sentence_start': 'Ү', 'other': 'ү'}
    },
    '/e/': {
        'ULY': {'sentence_start': 'Ë', 'other': 'ë'},
        'UYY': {'sentence_start': 'E', 'other': 'e'},
        'UEY': {
            'Base': 'ې', #U+0x06D0
            'Isolated': 'ئې',
            'Simple Isolated': 'ې', # U+0xFBE4
            'Initial': 'ﺋﯦ',
            'Simple Initial': 'ﯦ', # U+0xFBE6
            'Medial': 'ﯧ', # U+0xFBE7
            'Medial Simple': '',
            'Final': 'ﯥ', # U+0xFBE5
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Е', 'other': 'е'}
    },
    '/i/': {
        'ULY': {'sentence_start': 'I', 'other': 'i'},
        'UYY': {'sentence_start': 'I', 'other': 'i'},
        'UEY': {
            'Base': 'ى', # U+0x0649
            'Isolated': 'ئى',
            'Simple Isolated': 'ﻯ', # U+0xFEEF
            'Initial': 'ﺋﯨ',
            'Simple Initial': 'ﯨ', # U+0xFBE8
            'Medial': 'ﯩ', # U+0xFBE9
            'Medial Simple': 'ﺌﯩ',
            'Final': 'ﻰ', # U+0xFEF0
            'Separated Final': 'ﺌﻰ'},
        'UKY': {'sentence_start': 'И', 'other': 'и'}
    },
    '/ɨ/':  {
        'ULY': {'sentence_start': 'I', 'other': 'i'},
        'UYY': {'sentence_start': 'I', 'other': 'i'},
        'UEY': {
            'Base': 'ى', # U+0x0649
            'Isolated': 'ئى',
            'Simple Isolated': 'ﻯ', # U+0xFEEF
            'Initial': 'ﺋﯨ',
            'Simple Initial': 'ﯨ', # U+0xFBE8
            'Medial': 'ﯩ', # U+0xFBE9
            'Medial Simple': 'ﺌﯩ',
            'Final': 'ﻰ', # U+0xFEF0
            'Separated Final': 'ﺌﻰ'},
        'UKY': {'sentence_start': 'И', 'other': 'и'}
    },
    '/b/': {
        'ULY': {'sentence_start': 'B', 'other': 'b'},
        'UYY': {'sentence_start': 'Б', 'other': 'б'},
        'UEY': {
            'Base': 'ب', #U+0x0628
            'Isolated': 'ﺏ', # U+0xFE8F
            'Simple Isolated': '',
            'Initial': 'ﺑ', # U+0xFE91
            'Simple Initial': '',
            'Medial': 'ﺒ', # U+0xFE92
            'Medial Simple': '',
            'Final': 'ﺐ', # U+0xFE90
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Б', 'other': 'б'}
    },
    '/p/': {
        'ULY': {'sentence_start': 'P', 'other': 'p'},
        'UYY': {'sentence_start': 'P', 'other': 'p'},
        'UEY': {
            'Base': 'پ', # U+0x067E
            'Isolated': 'ﭖ', # U+0xFB56
            'Simple Isolated': '',
            'Initial': 'ﭘ', # U+0xFB58
            'Simple Initial': '',
            'Medial': 'ﭙ', # U+0xFB59
            'Medial Simple': '',
            'Final': 'ﭗ', # U+0xFB57
            'Separated Final': ''
        },
        'UKY': {'sentence_start': 'П', 'other': 'п'}
    },
    '/t/': {
        'ULY': {'sentence_start': 'T', 'other': 't'},
        'UYY': {'sentence_start': 'T', 'other': 't'},
        'UEY': {
            'Base': 'ت', # U+0x062A
            'Isolated': 'ﺕ', # U+0xFE95
                'Simple Isolated': '',
                'Initial': 'ﺗ', # U+0xFE97
                'Simple Initial': '',
                'Medial': 'ﺘ', # U+0xFE98
                'Medial Simple': '',
                'Final': 'ﺖ', # U+0xFE96
                'Separated Final': ''},
        'UKY': {'sentence_start': 'Т', 'other': 'т'}
    },
    'd͡ʒ': {
        'ULY': {'sentence_start': 'J', 'other': 'j'},
        'UYY': {'sentence_start': 'J', 'other': 'j'},
        'UEY': {
            'Base': 'ج', # U+0x062C
            'Isolated': 'ﺝ', # U+0xFE9D
            'Simple Isolated': '',
            'Initial': 'ﺟ', # U+0xFE9F
            'Simple Initial': '',
            'Medial': 'ﺠ', # U+0xFEA0
            'Medial Simple': '',
            'Final': 'ﺞ', # U+0xFE9E
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Җ', 'other': 'җ'}
    },
    'dʒ': {
        'ULY': {'sentence_start': 'J', 'other': 'j'},
        'UYY': {'sentence_start': 'J', 'other': 'j'},
        'UEY': {
            'Base': 'ج', # U+0x062C
            'Isolated': 'ﺝ', # U+0xFE9D
            'Simple Isolated': '',
            'Initial': 'ﺟ', # U+0xFE9F
            'Simple Initial': '',
            'Medial': 'ﺠ', # U+0xFEA0
            'Medial Simple': '',
            'Final': 'ﺞ', # U+0xFE9E
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Җ', 'other': 'җ'}
    },
    '/t͡ʃ/': {
        'ULY': {'sentence_start': 'Ch', 'other': 'ch'},
        'UYY': {'sentence_start': 'Q', 'other': 'q'},
        'UEY': {
            'Base': 'چ', # U+0x0686
            'Isolated': 'ﭺ', # U+0xFB7A
            'Simple Isolated': '',
            'Initial': 'ﭼ', # U+0xFB7C
            'Simple Initial': '',
            'Medial': 'ﭽ', # U+0xFB7D
            'Medial Simple': '',
            'Final': 'ﭻ', # U+0xFB7B
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ч', 'other': 'ч'}
    },
    '/tʃ/': {
        'ULY': {'sentence_start': 'Ch', 'other': 'ch'},
        'UYY': {'sentence_start': 'Q', 'other': 'q'},
        'UEY': {
            'Base': 'چ', # U+0x0686
            'Isolated': 'ﭺ', # U+0xFB7A
            'Simple Isolated': '',
            'Initial': 'ﭼ', # U+0xFB7C
            'Simple Initial': '',
            'Medial': 'ﭽ', # U+0xFB7D
            'Medial Simple': '',
            'Final': 'ﭻ', # U+0xFB7B
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ч', 'other': 'ч'}
    },
    '/χ/': {
        'ULY': {'sentence_start': 'X', 'other': 'x'},
        'UYY': {'sentence_start': 'H', 'other': 'h'},
        'UEY': {
            'Base': 'خ', # U+0x062E
            'Isolated': 'ﺥ', # U+0xFEA5
            'Simple Isolated': '',
            'Initial': 'ﺧ', # U+0xFEA7
            'Simple Initial': '',
            'Medial': 'ﺨ ', # U+0xFEA8
            'Medial Simple': '',
            'Final': 'ﺦ', # U+0xFEA6
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Х', 'other': 'х'}
    },
    '/d/': {
        'ULY': {'sentence_start': 'D', 'other': 'd'},
        'UYY': {'sentence_start': 'D', 'other': 'd'},
        'UEY': {
            'Base': 'د', # U+0x062F
            'Isolated': 'د', # U+0x062F
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﺪ', # U+0xFEAA
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Д', 'other': 'д'}
    },
    '/r/': {
        'ULY': {'sentence_start': 'R', 'other': 'r'},
        'UYY': {'sentence_start': 'R', 'other': 'r'},
        'UEY': {
            'Base':'ر', # U+0x0631
            'Isolated': 'ر', # U+0x0631
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﺮ', # U+0xFEAE
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Р', 'other': 'р'}
    },
    '/z/': {
        'ULY': {'sentence_start': 'Z', 'other': 'z'},
        'UYY': {'sentence_start': 'Z', 'other': 'z'},
        'UEY': {
            'Base':'ز', # U+0x0632
            'Isolated': 'ﺯ',  # U+0xFEAF
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﺰ', # U+0xFEB0
            'Separated Final': ''},
        'UKY': {'sentence_start': 'З', 'other': 'з'}
    },
    '/ʒ/': {
        'ULY': {'sentence_start': 'Zh', 'other': 'zh'},
        'UYY': {'sentence_start': 'Ⱬ', 'other': 'ⱬ'},
        'UEY': {
            'Base': 'ژ',    # U+0698
            'Isolated': 'ﮊ',# U+0xFB8A
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﮋ',   # U+0xFB8B
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ж', 'other': 'ж'}
    },
    '/ʃ/': {
        'ULY': {'sentence_start': 'Sh', 'other': 'sh'},
        'UYY': {'sentence_start': 'X', 'other': 'x'},
        'UEY': {
            'Base': 'ش', # U+0x0634
            'Isolated': 'ﺵ', # U+0xFEB5
            'Simple Isolated': '',
            'Initial': 'ﺳ', # U+0xFEB3
            'Simple Initial': '',
            'Medial': 'ﺴ', # U+0xFEB4
            'Medial Simple': '',
            'Final': 'ﺲ', # U+0xFEB2
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ш', 'other': 'ш'}
    },
    '/ʁ/': {
        'ULY': {'sentence_start': 'Gh', 'other': 'gh'},
        'UYY': {'sentence_start': 'Ƣ', 'other': 'ƣ'},
        'UEY': {
            'Base':'غ',# 063a
            'Isolated': 'ﻍ', # fecd
            'Simple Isolated': '',
            'Initial': 'ﻏ', # fecf
            'Simple Initial': '',
            'Medial': 'ﻐ', # fed0
            'Medial Simple': '',
            'Final': 'ﻎ', #fece
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ғ', 'other': 'ғ'}
    },
    '/f/': {
        'ULY': {'sentence_start': 'F', 'other': 'f'},
        'UYY': {'sentence_start': 'F', 'other': 'f'},
        'UEY': {
            'Base':'ف', # 0641
            'Isolated': 'ﻑ', #fed1
            'Simple Isolated': '',
            'Initial': 'ﻓ', # fed3
            'Simple Initial': '',
            'Medial': 'ﻔ', #fed4
            'Medial Simple': '',
            'Final': 'ﻒ', #fed2
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ф', 'other': 'ф'}
    },
    '/q/': {
        'ULY': {'sentence_start': 'Q', 'other': 'q'},
        'UYY': {'sentence_start': 'Ⱪ', 'other': 'ⱪ'},
        'UEY': {
            'Base':'ق', # 0642
            'Isolated': 'ﻕ', # fed5
            'Simple Isolated': '',
            'Initial': 'ﻗ', # fed7
            'Simple Initial': '',
            'Medial': 'ﻘ', # fed8
            'Medial Simple': '',
            'Final': 'ﻖ', # fed6
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Қ', 'other': 'қ'}
    },
    '/k/': {
        'ULY': {'sentence_start': 'K', 'other': 'k'},
        'UYY': {'sentence_start': 'K', 'other': 'k'},
        'UEY': {
            'Base':'ك', # 0643
            'Isolated': 'ﻙ', # fed9
            'Simple Isolated': '',
            'Initial': 'ﻛ', # fedb
            'Simple Initial': '',
            'Medial': 'ﻜ', # fedc
            'Medial Simple': '',
            'Final': 'ﻚ', #  feda
            'Separated Final': ''},
        'UKY': {'sentence_start': 'К', 'other': 'к'}
    },
    '/ɡ/': {
        'ULY': {'sentence_start': 'G', 'other': 'g'},
        'UYY': {'sentence_start': 'G', 'other': 'g'},
        'UEY': {
            'Base': 'گ', #  06af
            'Isolated': 'ﮒ', # fb92
            'Simple Isolated': '',
            'Initial': 'ﮔ', # fb94
            'Simple Initial': '',
            'Medial': 'ﮕ', #  fb95
            'Medial Simple': '',
            'Final': 'ﮓ', # fb93
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Г', 'other': 'г'}
    },
    '/ŋ/': {
        'ULY': {'sentence_start': 'Ng', 'other': 'ng'},
        'UYY': {'sentence_start': 'Ng', 'other': 'ng'},
        'UEY': {
            'Base': 'ڭ', # 06AD
            'Isolated': 'ﯓ', # fbd3
            'Simple Isolated': '',
            'Initial': 'ﯕ', # fbd5
            'Simple Initial': '',
            'Medial': 'ﯖ', #  fbd6
            'Medial Simple': '',
            'Final': 'ﯔ', # fbd4
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ң', 'other': 'ң'}
    },
    '/l/': {
        'ULY': {'sentence_start': 'L', 'other': 'l'},
        'UYY': {'sentence_start': 'L', 'other': 'l'},
        'UEY': {
            'Base': 'ل', # 0644
            'Isolated': 'ﻝ', # fedd
            'Simple Isolated': '',
            'Initial': 'ﻟ', # fedf
            'Simple Initial': '',
            'Medial': 'ﻠ', #  fee0
            'Medial Simple': '',
            'Final': 'ﻞ', # fede
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Л', 'other': 'л'}
    },
    '/m/': {
        'ULY': {'sentence_start': 'M', 'other': 'm'},
        'UYY': {'sentence_start': 'M', 'other': 'm'},
        'UEY': {
            'Base':'م',# 0645
            'Isolated': 'ﻡ', # fee1
            'Simple Isolated': '',
            'Initial': 'ﻣ', # fee3
            'Simple Initial': '',
            'Medial': 'ﻤ', # fee4
            'Medial Simple': '',
            'Final': 'ﻢ', # fee2
            'Separated Final': ''},
        'UKY': {'sentence_start': 'М', 'other': 'м'}
    },
    '/n/': {
        'ULY': {'sentence_start': 'N', 'other': 'n'},
        'UYY': {'sentence_start': 'N', 'other': 'n'},
        'UEY': {
            'Base':'ن',# 0646
            'Isolated': 'ﻥ',#  fee5
            'Simple Isolated': '',
            'Initial': 'ﻧ', # fee7
            'Simple Initial': '',
            'Medial': 'ﻨ', # fee8
            'Medial Simple': '',
            'Final': 'ﻦ',# fee6
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Н', 'other': 'н'}
    },
    '/h/': {
        'ULY': {'sentence_start': 'H', 'other': 'h'},
        'UYY': {'sentence_start': 'Ⱨ', 'other': 'ⱨ'},
        'UEY': {
            'Base': 'ھ',# 06be
            'Isolated': 'ﮪ', # fbaa
            'Simple Isolated': '',
            'Initial': 'ﮬ', # fbac
            'Simple Initial': '',
            'Medial': 'ﮭ', # fbad
            'Medial Simple': '',
            'Final': 'ﮫ', # U+FBAB   这个字母会显示成 U+0xFEEA(ﻪ) 的样子 可能时字体的错误
            'Separated Final': ''
        },
        'UKY': {'sentence_start': 'Һ', 'other': 'һ'}},
    '/w/': {
        'ULY': {'sentence_start': 'W', 'other': 'w'},
        'UYY': {'sentence_start': 'W', 'other': 'w'},
        'UEY': {
            'Base':'ۋ',# 06cb
            'Isolated': 'ﯞ', # fbde
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﯟ',# fbdf
            'Separated Final': ''
        },
        'UKY': {'sentence_start': 'В', 'other': 'в'}
    },
    '/v/': {
        'ULY': {'sentence_start': 'W', 'other': 'w'},
        'UYY': {'sentence_start': 'V', 'other': 'v'},
        'UEY': {
            'Base':'ۋ',# 06cb
            'Isolated': 'ﯞ', # fbde
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': 'ﯟ',# fbdf
            'Separated Final': ''
        },
        'UKY': {'sentence_start': 'В', 'other': 'в'}
    },
    '/j/': {
        'ULY': {'sentence_start': 'Y', 'other': 'y'},
        'UYY': {'sentence_start': 'Y', 'other': 'y'},
        'UEY': {
            'Base': 'ي', #  064a
            'Isolated': 'ﻱ', # fef1
            'Simple Isolated': '',
            'Initial': 'ﻳ', # fef3
            'Simple Initial': '',
            'Medial': 'ﻴ', # fef4
            'Medial Simple': '',
            'Final': 'ﻲ', # fef2
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Й', 'other': 'й'}
    },
#   西里尔维文多了两个字母 Ю(ي‍‍ۇ) Я(ي‍‍ا)
'/ju/': {
        'ULY': {'sentence_start': 'YU', 'other': 'yu'},
        'UYY': {'sentence_start': 'YU', 'other': 'yu'},
        'UEY': {
            'Base': 'ي‍‍ۇ',
            'Isolated': 'ي‍‍ۇ',
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': '',
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Ю', 'other': 'ю'}
    },
'/ja/': {
        'ULY': {'sentence_start': 'YA', 'other': 'ya'},
        'UYY': {'sentence_start': 'YA', 'other': 'ya'},
        'UEY': {
            'Base': 'ي‍‍ا',
            'Isolated': 'ي‍‍ا',
            'Simple Isolated': '',
            'Initial': '',
            'Simple Initial': '',
            'Medial': '',
            'Medial Simple': '',
            'Final': '',
            'Separated Final': ''},
        'UKY': {'sentence_start': 'Я', 'other': 'я'}
    }
}




