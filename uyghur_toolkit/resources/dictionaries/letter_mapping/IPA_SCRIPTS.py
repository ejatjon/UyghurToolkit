#  老维文UEY符号ئ（\u0626） 拉丁ULY(’) 不存在UYY,UKY,IPA 的对应表示

IPA_SCRIPTS = {
    '\u0251': {  # ɑ
        'ULY': {'sentence_start': '\u0041', 'other': '\u0061'},  # {'sentence_start': 'A', 'other': 'a'}
        'UYY': {'sentence_start': '\u0041', 'other': '\u0061'},  # {'sentence_start': 'A', 'other': 'a'}
        'UEY': {
            'Base': '\u0627',  # ا
            'Isolated': '\uFE8B\ufe8e',  # ئا
            'Simple Isolated': '\ufe8d',  # ﺍ
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufe8e',  # ﺎ
            'Separated Final': '\ufe8c\ufe8e',  # ﺌﺎ
        },
        'UKY': {'sentence_start': '\u0410', 'other': '\u0430'},  # {'sentence_start': 'А', 'other': 'а'}
    },

    '\u025b': {  # ɛ
        'ULY': {'sentence_start': '\u0045', 'other': '\u0065'},  # {'sentence_start': 'E', 'other': 'e'}
        'UYY': {'sentence_start': '\u018f', 'other': '\u0259'},  # {'sentence_start': 'Ə', 'other': 'ə'}
        'UEY': {
            'Base': '\u06d5',  # ە
            'Isolated': '\uFE8B\ufeea',  # ئە
            'Simple Isolated': '\ufee9',  # ﻩ
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufeea',  # ﻪ
            'Separated Final': '\ufe8c\ufeea',  # ﺌﻪ
        },
        'UKY': {'sentence_start': '\u04d8', 'other': '\u04d9'},  # {'sentence_start': 'Ә', 'other': 'ә'}
    },

    '\u00e6': {  # æ
        'ULY': {'sentence_start': '\u0045', 'other': '\u0065'},  # {'sentence_start': 'E', 'other': 'e'}
        'UYY': {'sentence_start': '\u018f', 'other': '\u0259'},  # {'sentence_start': 'Ə', 'other': 'ə'}
        'UEY': {
            'Base': '\u06d5',  # ە
            'Isolated': '\uFE8B\ufeea',  # ئە
            'Simple Isolated': '\ufee9',  # ﻩ
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufeea',  # ﻪ
            'Separated Final': '\ufe8c\ufeea',  # ﺌﻪ
        },
        'UKY': {'sentence_start': '\u04d8', 'other': '\u04d9'},  # {'sentence_start': 'Ә', 'other': 'ә'}
    },

    '\u006f': {  # o
        'ULY': {'sentence_start': '\u004f', 'other': '\u006f'},  # {'sentence_start': 'O', 'other': 'o'}
        'UYY': {'sentence_start': '\u004f', 'other': '\u006f'},  # {'sentence_start': 'O', 'other': 'o'}
        'UEY': {
            'Base': '\u0648',  # و
            'Isolated': '\uFE8B\ufeee',  # ئو
            'Simple Isolated': '\ufeed',  # ﻭ
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufeee',  # ﻮ
            'Separated Final': '\ufe8c\ufeee',  # ﺌﻮ
        },
        'UKY': {'sentence_start': '\u041e', 'other': '\u043e'},  # {'sentence_start': 'О', 'other': 'о'}
    },

    '\u0075': {  # u
        'ULY': {'sentence_start': '\u0055', 'other': '\u0075'},  # {'sentence_start': 'U', 'other': 'u'}
        'UYY': {'sentence_start': '\u0055', 'other': '\u0075'},  # {'sentence_start': 'U', 'other': 'u'}
        'UEY': {
            'Base': '\u06c7',  # ۇ
            'Isolated': '\uFE8B\ufbd8',  # ئۇ
            'Simple Isolated': '\ufbd7',  # ﯗ
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufbd8',  # ﯘ
            'Separated Final': '\ufe8c\ufbd8',  # ﺌﯘ
        },
        'UKY': {'sentence_start': '\u0423', 'other': '\u0443'},  # {'sentence_start': 'У', 'other': 'у'}
    },

    '\u00f8': {  # ø
        'ULY': {'sentence_start': '\u00d6', 'other': '\u00f6'},  # {'sentence_start': 'Ö', 'other': 'ö'}
        'UYY': {'sentence_start': '\u019f', 'other': '\u0275'},  # {'sentence_start': 'Ɵ', 'other': 'ɵ'}
        'UEY': {
            'Base': '\u06c6',  # ۆ
            'Isolated': '\uFE8B\ufbda',  # ئۆ
            'Simple Isolated': '\ufbd9',  # ﯙ
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufbda',  # ﯚ
            'Separated Final': '',  # (ﺌﯚ) 维语好像没有这种用法的词其他也一样
        },
        'UKY': {'sentence_start': '\u04e8', 'other': '\u04e9'},  # {'sentence_start': 'Ө', 'other': 'ө'}
    },

    '\u0079': {  # y
        'ULY': {'sentence_start': '\u00dc', 'other': '\u00fc'},  # {'sentence_start': 'Ü', 'other': 'ü'}
        'UYY': {'sentence_start': '\u00dc', 'other': '\u00fc'},  # {'sentence_start': 'Ü', 'other': 'ü'}
        'UEY': {
            'Base': '\u06c8',  # ۈ
            'Isolated': '\uFE8B\ufbdc',  # ئۈ
            'Simple Isolated': '\ufbdb',  # ﯛ
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufbdc',  # ﯜ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u04ae', 'other': '\u04af'},  # {'sentence_start': 'Ү', 'other': 'ү'}
    },

    '\u0065': {  # e
        'ULY': {'sentence_start': '\u00cb', 'other': '\u00eb'},  # {'sentence_start': 'Ë', 'other': 'ë'}
        'UYY': {'sentence_start': '\u0045', 'other': '\u0065'},  # {'sentence_start': 'E', 'other': 'e'}
        'UEY': {
            'Base': '\u06d0',  # ې
            'Isolated': '\uFE8B\ufbe5',  # ئې
            'Simple Isolated': '\u06d0',  # ې
            'Initial': '\ufe8b\ufbe6',  # ﺋﯦ
            'Simple Initial': '\ufbe6',  # ﯦ
            'Medial': '\ufbe7',  # ﯧ
            'Separated Medial': '',  #
            'Final': '\ufbe5',  # ﯥ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0415', 'other': '\u0435'},  # {'sentence_start': 'Е', 'other': 'е'}
    },

    '\u0069': {  # i
        'ULY': {'sentence_start': '\u0049', 'other': '\u0069'},  # {'sentence_start': 'I', 'other': 'i'}
        'UYY': {'sentence_start': '\u0049', 'other': '\u0069'},  # {'sentence_start': 'I', 'other': 'i'}
        'UEY': {
            'Base': '\u0649',  # ى
            'Isolated': '\uFE8B\ufef0',  # ئى
            'Simple Isolated': '\ufeef',  # ﻯ
            'Initial': '\ufe8b\ufbe8',  # ﺋﯨ
            'Simple Initial': '\ufbe8',  # ﯨ
            'Medial': '\ufbe9',  # ﯩ
            'Separated Medial': '\ufe8c\ufbe9',  # ﺌﯩ
            'Final': '\ufef0',  # ﻰ
            'Separated Final': '\ufe8c\ufef0',  # ﺌﻰ
        },
        'UKY': {'sentence_start': '\u0418', 'other': '\u0438'},  # {'sentence_start': 'И', 'other': 'и'}
    },

    '\u0268': {  # ɨ
        'ULY': {'sentence_start': '\u0049', 'other': '\u0069'},  # {'sentence_start': 'I', 'other': 'i'}
        'UYY': {'sentence_start': '\u0049', 'other': '\u0069'},  # {'sentence_start': 'I', 'other': 'i'}
        'UEY': {
            'Base': '\u0649',  # ى
            'Isolated': '\uFE8B\ufef0',  # ئى
            'Simple Isolated': '\ufeef',  # ﻯ
            'Initial': '\ufe8b\ufbe8',  # ﺋﯨ
            'Simple Initial': '\ufbe8',  # ﯨ
            'Medial': '\ufbe9',  # ﯩ
            'Separated Medial': '\ufe8c\ufbe9',  # ﺌﯩ
            'Final': '\ufef0',  # ﻰ
            'Separated Final': '\ufe8c\ufef0',  # ﺌﻰ
        },
        'UKY': {'sentence_start': '\u0418', 'other': '\u0438'},  # {'sentence_start': 'И', 'other': 'и'}
    },

    '\u0062': {  # b
        'ULY': {'sentence_start': '\u0042', 'other': '\u0062'},  # {'sentence_start': 'B', 'other': 'b'}
        'UYY': {'sentence_start': '\u0042', 'other': '\u0062'},  # {'sentence_start': 'B', 'other': 'b'}
        'UEY': {
            'Base': '\u0628',  # ب
            'Isolated': '\ufe8f',  # ﺏ
            'Simple Isolated': '',  #
            'Initial': '\ufe91',  # ﺑ
            'Simple Initial': '',  #
            'Medial': '\ufe92',  # ﺒ
            'Separated Medial': '',  #
            'Final': '\ufe90',  # ﺐ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0411', 'other': '\u0431'},  # {'sentence_start': 'Б', 'other': 'б'}
    },

    '\u0070': {  # p
        'ULY': {'sentence_start': '\u0050', 'other': '\u0070'},  # {'sentence_start': 'P', 'other': 'p'}
        'UYY': {'sentence_start': '\u0050', 'other': '\u0070'},  # {'sentence_start': 'P', 'other': 'p'}
        'UEY': {
            'Base': '\u067e',  # پ
            'Isolated': '\ufb56',  # ﭖ
            'Simple Isolated': '',  #
            'Initial': '\ufb58',  # ﭘ
            'Simple Initial': '',  #
            'Medial': '\ufb59',  # ﭙ
            'Separated Medial': '',  #
            'Final': '\ufb57',  # ﭗ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u041f', 'other': '\u043f'},  # {'sentence_start': 'П', 'other': 'п'}
    },

    '\u0074': {  # t
        'ULY': {'sentence_start': '\u0054', 'other': '\u0074'},  # {'sentence_start': 'T', 'other': 't'}
        'UYY': {'sentence_start': '\u0054', 'other': '\u0074'},  # {'sentence_start': 'T', 'other': 't'}
        'UEY': {
            'Base': '\u062a',  # ت
            'Isolated': '\ufe95',  # ﺕ
            'Simple Isolated': '',  #
            'Initial': '\ufe97',  # ﺗ
            'Simple Initial': '',  #
            'Medial': '\ufe98',  # ﺘ
            'Separated Medial': '',  #
            'Final': '\ufe96',  # ﺖ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0422', 'other': '\u0442'},  # {'sentence_start': 'Т', 'other': 'т'}
    },

    '\u0064\u0361\u0292': {  # d͡ʒ
        'ULY': {'sentence_start': '\u004a', 'other': '\u006a'},  # {'sentence_start': 'J', 'other': 'j'}
        'UYY': {'sentence_start': '\u004a', 'other': '\u006a'},  # {'sentence_start': 'J', 'other': 'j'}
        'UEY': {
            'Base': '\u062c',  # ج
            'Isolated': '\ufe9d',  # ﺝ
            'Simple Isolated': '',  #
            'Initial': '\ufe9f',  # ﺟ
            'Simple Initial': '',  #
            'Medial': '\ufea0',  # ﺠ
            'Separated Medial': '',  #
            'Final': '\ufe9e',  # ﺞ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0496', 'other': '\u0497'},  # {'sentence_start': 'Җ', 'other': 'җ'}
    },

    '\u0074\u0361\u0283': {  # t͡ʃ
        'ULY': {'sentence_start': '\u0043\u0068', 'other': '\u0063\u0068'},
        # {'sentence_start': 'Ch', 'other': 'ch'}
        'UYY': {'sentence_start': '\u0051', 'other': '\u0071'},  # {'sentence_start': 'Q', 'other': 'q'}
        'UEY': {
            'Base': '\u0686',  # چ
            'Isolated': '\ufb7a',  # ﭺ
            'Simple Isolated': '',  #
            'Initial': '\ufb7c',  # ﭼ
            'Simple Initial': '',  #
            'Medial': '\ufb7d',  # ﭽ
            'Separated Medial': '',  #
            'Final': '\ufb7b',  # ﭻ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0427', 'other': '\u0447'},  # {'sentence_start': 'Ч', 'other': 'ч'}
    },
    '\u03c7': {  # χ
        'ULY': {'sentence_start': '\u0058', 'other': '\u0078'},  # {'sentence_start': 'X', 'other': 'x'}
        'UYY': {'sentence_start': '\u0048', 'other': '\u0068'},  # {'sentence_start': 'H', 'other': 'h'}
        'UEY': {
            'Base': '\u062e',  # خ
            'Isolated': '\ufea5',  # ﺥ
            'Simple Isolated': '',  #
            'Initial': '\ufea7',  # ﺧ
            'Simple Initial': '',  #
            'Medial': '\ufea8',  # ﺨ
            'Separated Medial': '',  #
            'Final': '\ufea6',  # ﺦ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0425', 'other': '\u0445'},  # {'sentence_start': 'Х', 'other': 'х'}
    },

    '\u0064': {  # d
        'ULY': {'sentence_start': '\u0044', 'other': '\u0064'},  # {'sentence_start': 'D', 'other': 'd'}
        'UYY': {'sentence_start': '\u0044', 'other': '\u0064'},  # {'sentence_start': 'D', 'other': 'd'}
        'UEY': {
            'Base': '\u062f',  # د
            'Isolated': '\u062f',  # د
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufeaa',  # ﺪ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0414', 'other': '\u0434'},  # {'sentence_start': 'Д', 'other': 'д'}
    },

    '\u0072': {  # r
        'ULY': {'sentence_start': '\u0052', 'other': '\u0072'},  # {'sentence_start': 'R', 'other': 'r'}
        'UYY': {'sentence_start': '\u0052', 'other': '\u0072'},  # {'sentence_start': 'R', 'other': 'r'}
        'UEY': {
            'Base': '\u0631',  # ر
            'Isolated': '\u0631',  # ر
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufeae',  # ﺮ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0420', 'other': '\u0440'},  # {'sentence_start': 'Р', 'other': 'р'}
    },

    '\u007a': {  # z
        'ULY': {'sentence_start': '\u005a', 'other': '\u007a'},  # {'sentence_start': 'Z', 'other': 'z'}
        'UYY': {'sentence_start': '\u005a', 'other': '\u007a'},  # {'sentence_start': 'Z', 'other': 'z'}
        'UEY': {
            'Base': '\u0632',  # ز
            'Isolated': '\ufeaf',  # ﺯ
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufeb0',  # ﺰ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0417', 'other': '\u0437'},  # {'sentence_start': 'З', 'other': 'з'}
    },

    '\u0292': {  # ʒ
        'ULY': {'sentence_start': '\u005a\u0068', 'other': '\u007a\u0068'},
        # {'sentence_start': 'Zh', 'other': 'zh'}
        'UYY': {'sentence_start': '\u2c6b', 'other': '\u2c6c'},  # {'sentence_start': 'Ⱬ', 'other': 'ⱬ'}
        'UEY': {
            'Base': '\u0698',  # ژ
            'Isolated': '\ufb8a',  # ﮊ
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufb8b',  # ﮋ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0416', 'other': '\u0436'},  # {'sentence_start': 'Ж', 'other': 'ж'}
    },
    '\u0073':{'ULY': {'sentence_start': '\u0053', 'other': '\u0073'},# {'sentence_start': 'S', 'other': 's'}
        'UYY': {'sentence_start': '\u0053', 'other': '\u0073'},  # {'sentence_start': 'S', 'other': 's'}
        'UEY': {
            'Base': '\u0633',  # س
            'Isolated': '\ufeb1',  # ﺱ
            'Simple Isolated': '',  #
            'Initial': '\ufeb3',  # ﺳ
            'Simple Initial': '',  #
            'Medial': '\ufeb4',  # ﺴ
            'Separated Medial': '',  #
            'Final': '\ufeb2',  # ﺲ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0421', 'other': '\u0441'},  # {'sentence_start': 'С', 'other': 'с'}
    },

    '\u0283': {  # ʃ
        'ULY': {'sentence_start': '\u0053\u0068', 'other': '\u0073\u0068'}, # {'sentence_start': 'Sh', 'other': 'sh'}
        'UYY': {'sentence_start': '\u0058', 'other': '\u0078'},  # {'sentence_start': 'X', 'other': 'x'}
        'UEY': {
            'Base': '\u0634',  # ش
            'Isolated': '\ufeb5',  # ﺵ
            'Simple Isolated': '',  #
            'Initial': '\ufeb7',  # ﺷ
            'Simple Initial': '',  #
            'Medial': '\ufeb8',  # ﺸ
            'Separated Medial': '',  #
            'Final': '\ufeb6',  # ﺶ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0428', 'other': '\u0448'},  # {'sentence_start': 'Ш', 'other': 'ш'}
    },

    '\u0281': {  # ʁ
        'ULY': {'sentence_start': '\u0047\u0068', 'other': '\u0067\u0068'},
        # {'sentence_start': 'Gh', 'other': 'gh'}
        'UYY': {'sentence_start': '\u01a2', 'other': '\u01a3'},  # {'sentence_start': 'Ƣ', 'other': 'ƣ'}
        'UEY': {
            'Base': '\u063a',  # غ
            'Isolated': '\ufecd',  # ﻍ
            'Simple Isolated': '',  #
            'Initial': '\ufecf',  # ﻏ
            'Simple Initial': '',  #
            'Medial': '\ufed0',  # ﻐ
            'Separated Medial': '',  #
            'Final': '\ufece',  # ﻎ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0492', 'other': '\u0493'},  # {'sentence_start': 'Ғ', 'other': 'ғ'}
    },

    '\u0066': {  # f
        'ULY': {'sentence_start': '\u0046', 'other': '\u0066'},  # {'sentence_start': 'F', 'other': 'f'}
        'UYY': {'sentence_start': '\u0046', 'other': '\u0066'},  # {'sentence_start': 'F', 'other': 'f'}
        'UEY': {
            'Base': '\u0641',  # ف
            'Isolated': '\ufed1',  # ﻑ
            'Simple Isolated': '',  #
            'Initial': '\ufed3',  # ﻓ
            'Simple Initial': '',  #
            'Medial': '\ufed4',  # ﻔ
            'Separated Medial': '',  #
            'Final': '\ufed2',  # ﻒ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0424', 'other': '\u0444'},  # {'sentence_start': 'Ф', 'other': 'ф'}
    },

    '\u0071': {  # q
        'ULY': {'sentence_start': '\u0051', 'other': '\u0071'},  # {'sentence_start': 'Q', 'other': 'q'}
        'UYY': {'sentence_start': '\u2c69', 'other': '\u2c6a'},  # {'sentence_start': 'Ⱪ', 'other': 'ⱪ'}
        'UEY': {
            'Base': '\u0642',  # ق
            'Isolated': '\ufed5',  # ﻕ
            'Simple Isolated': '',  #
            'Initial': '\ufed7',  # ﻗ
            'Simple Initial': '',  #
            'Medial': '\ufed8',  # ﻘ
            'Separated Medial': '',  #
            'Final': '\ufed6',  # ﻖ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u049a', 'other': '\u049b'},  # {'sentence_start': 'Қ', 'other': 'қ'}
    },

    '\u006b': {  # k
        'ULY': {'sentence_start': '\u004b', 'other': '\u006b'},  # {'sentence_start': 'K', 'other': 'k'}
        'UYY': {'sentence_start': '\u004b', 'other': '\u006b'},  # {'sentence_start': 'K', 'other': 'k'}
        'UEY': {
            'Base': '\u0643',  # ك
            'Isolated': '\ufed9',  # ﻙ
            'Simple Isolated': '',  #
            'Initial': '\ufedb',  # ﻛ
            'Simple Initial': '',  #
            'Medial': '\ufedc',  # ﻜ
            'Separated Medial': '',  #
            'Final': '\ufeda',  # ﻚ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u041a', 'other': '\u043a'},  # {'sentence_start': 'К', 'other': 'к'}
    },

    '\u0261': {  # ɡ
        'ULY': {'sentence_start': '\u0047', 'other': '\u0067'},  # {'sentence_start': 'G', 'other': 'g'}
        'UYY': {'sentence_start': '\u0047', 'other': '\u0067'},  # {'sentence_start': 'G', 'other': 'g'}
        'UEY': {
            'Base': '\u06af',  # گ
            'Isolated': '\ufb92',  # ﮒ
            'Simple Isolated': '',  #
            'Initial': '\ufb94',  # ﮔ
            'Simple Initial': '',  #
            'Medial': '\ufb95',  # ﮕ
            'Separated Medial': '',  #
            'Final': '\ufb93',  # ﮓ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0413', 'other': '\u0433'},  # {'sentence_start': 'Г', 'other': 'г'}
    },

    '\u014b': {  # ŋ
        'ULY': {'sentence_start': '\u004e\u0067', 'other': '\u006e\u0067'},
        # {'sentence_start': 'Ng', 'other': 'ng'}
        'UYY': {'sentence_start': '\u004e\u0067', 'other': '\u006e\u0067'},
        # {'sentence_start': 'Ng', 'other': 'ng'}
        'UEY': {
            'Base': '\u06ad',  # ڭ
            'Isolated': '\ufbd3',  # ﯓ
            'Simple Isolated': '',  #
            'Initial': '\ufbd5',  # ﯕ
            'Simple Initial': '',  #
            'Medial': '\ufbd6',  # ﯖ
            'Separated Medial': '',  #
            'Final': '\ufbd4',  # ﯔ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u04a2', 'other': '\u04a3'},  # {'sentence_start': 'Ң', 'other': 'ң'}
    },

    '\u006c': {  # l
        'ULY': {'sentence_start': '\u004c', 'other': '\u006c'},  # {'sentence_start': 'L', 'other': 'l'}
        'UYY': {'sentence_start': '\u004c', 'other': '\u006c'},  # {'sentence_start': 'L', 'other': 'l'}
        'UEY': {
            'Base': '\u0644',  # ل
            'Isolated': '\ufedd',  # ﻝ
            'Simple Isolated': '',  #
            'Initial': '\ufedf',  # ﻟ
            'Simple Initial': '',  #
            'Medial': '\ufee0',  # ﻠ
            'Separated Medial': '',  #
            'Final': '\ufede',  # ﻞ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u041b', 'other': '\u043b'},  # {'sentence_start': 'Л', 'other': 'л'}
    },

    '\u006d': {  # m
        'ULY': {'sentence_start': '\u004d', 'other': '\u006d'},  # {'sentence_start': 'M', 'other': 'm'}
        'UYY': {'sentence_start': '\u004d', 'other': '\u006d'},  # {'sentence_start': 'M', 'other': 'm'}
        'UEY': {
            'Base': '\u0645',  # م
            'Isolated': '\ufee1',  # ﻡ
            'Simple Isolated': '',  #
            'Initial': '\ufee3',  # ﻣ
            'Simple Initial': '',  #
            'Medial': '\ufee4',  # ﻤ
            'Separated Medial': '',  #
            'Final': '\ufee2',  # ﻢ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u041c', 'other': '\u043c'},  # {'sentence_start': 'М', 'other': 'м'}
    },

    '\u006e': {  # n
        'ULY': {'sentence_start': '\u004e', 'other': '\u006e'},  # {'sentence_start': 'N', 'other': 'n'}
        'UYY': {'sentence_start': '\u004e', 'other': '\u006e'},  # {'sentence_start': 'N', 'other': 'n'}
        'UEY': {
            'Base': '\u0646',  # ن
            'Isolated': '\ufee5',  # ﻥ
            'Simple Isolated': '',  #
            'Initial': '\ufee7',  # ﻧ
            'Simple Initial': '',  #
            'Medial': '\ufee8',  # ﻨ
            'Separated Medial': '',  #
            'Final': '\ufee6',  # ﻦ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u041d', 'other': '\u043d'},  # {'sentence_start': 'Н', 'other': 'н'}
    },

    '\u0068': {  # h
        'ULY': {'sentence_start': '\u0048', 'other': '\u0068'},  # {'sentence_start': 'H', 'other': 'h'}
        'UYY': {'sentence_start': '\u2c67', 'other': '\u2c68'},  # {'sentence_start': 'Ⱨ', 'other': 'ⱨ'}
        'UEY': {
            'Base': '\u06be',  # ھ
            'Isolated': '\ufbaa',  # ﮪ
            'Simple Isolated': '',  #
            'Initial': '\ufbac',  # ﮬ
            'Simple Initial': '',  #
            'Medial': '\ufbad',  # ﮭ
            'Separated Medial': '',  #
            'Final': '\ufbab',  # ﮫ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u04ba', 'other': '\u04bb'},  # {'sentence_start': 'Һ', 'other': 'һ'}
    },

    '\u0077': {  # w
        'ULY': {'sentence_start': '\u0057', 'other': '\u0077'},  # {'sentence_start': 'W', 'other': 'w'}
        'UYY': {'sentence_start': '\u0057', 'other': '\u0077'},  # {'sentence_start': 'W', 'other': 'w'}
        'UEY': {
            'Base': '\u06cb',  # ۋ
            'Isolated': '\ufbde',  # ﯞ
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufbdf',  # ﯟ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0412', 'other': '\u0432'},  # {'sentence_start': 'В', 'other': 'в'}
    },

    '\u0076': {  # v
        'ULY': {'sentence_start': '\u0057', 'other': '\u0077'},  # {'sentence_start': 'W', 'other': 'w'}
        'UYY': {'sentence_start': '\u0056', 'other': '\u0076'},  # {'sentence_start': 'V', 'other': 'v'}
        'UEY': {
            'Base': '\u06cb',  # ۋ
            'Isolated': '\ufbde',  # ﯞ
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '\ufbdf',  # ﯟ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0412', 'other': '\u0432'},  # {'sentence_start': 'В', 'other': 'в'}
    },

    '\u006a': {  # j
        'ULY': {'sentence_start': '\u0059', 'other': '\u0079'},  # {'sentence_start': 'Y', 'other': 'y'}
        'UYY': {'sentence_start': '\u0059', 'other': '\u0079'},  # {'sentence_start': 'Y', 'other': 'y'}
        'UEY': {
            'Base': '\u064a',  # ي
            'Isolated': '\ufef1',  # ﻱ
            'Simple Isolated': '',  #
            'Initial': '\ufef3',  # ﻳ
            'Simple Initial': '',  #
            'Medial': '\ufef4',  # ﻴ
            'Separated Medial': '',  #
            'Final': '\ufef2',  # ﻲ
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u0419', 'other': '\u0439'},  # {'sentence_start': 'Й', 'other': 'й'}
    },
    # 西里尔维文多了两个字母 Ю(ي‍‍ۇ) Я(ي‍‍ا)
    '\u006a\u0075': {  # ju
        'ULY': {'sentence_start': '\u0059\u0055', 'other': '\u0079\u0075'},
        # {'sentence_start': 'YU', 'other': 'yu'}
        'UYY': {'sentence_start': '\u0059\u0055', 'other': '\u0079\u0075'},
        # {'sentence_start': 'YU', 'other': 'yu'}
        'UEY': {
            'Base': '\u064a\u06c7',  # ي‍‍ۇ
            'Isolated': '\u064a\u06c7',  # ي‍‍ۇ
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '',  #
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u042e', 'other': '\u044e'},  # {'sentence_start': 'Ю', 'other': 'ю'}
    },

    '\u006a\u0061': {  # ja
        'ULY': {'sentence_start': '\u0059\u0041', 'other': '\u0079\u0061'},
        # {'sentence_start': 'YA', 'other': 'ya'}
        'UYY': {'sentence_start': '\u0059\u0041', 'other': '\u0079\u0061'},
        # {'sentence_start': 'YA', 'other': 'ya'}
        'UEY': {
            'Base': '\u064a\u0627',  # ي‍‍ا
            'Isolated': '\u064a\u0627',  # ي‍‍ا
            'Simple Isolated': '',  #
            'Initial': '',  #
            'Simple Initial': '',  #
            'Medial': '',  #
            'Separated Medial': '',  #
            'Final': '',  #
            'Separated Final': '',  #
        },
        'UKY': {'sentence_start': '\u042f', 'other': '\u044f'},  # {'sentence_start': 'Я', 'other': 'я'}
    }

}




