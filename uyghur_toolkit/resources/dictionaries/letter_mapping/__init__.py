import json
from typing import MutableMapping
from uyghur_toolkit.resources.dictionaries.letter_mapping.IPA_SCRIPTS import IPA_SCRIPTS
'''
通过IPA_SCRIPTS 为生成其他四种映射
'''

def Uey():
    uey={}
    for k,v in IPA_SCRIPTS.items():
        key=v['UEY']['Base']
        if key in uey:
            uey[key]['IPA'].append(k)
            continue
        dd={}
        dd["IPA"]=[k]
        dd["UKY"]=v["UKY"]
        dd["ULY"] = v["ULY"]
        dd["UYY"] = v["UYY"]
        dd["UEY"] = v["UEY"]
        uey[key]= dd
    return uey

def UEY_latter_map():
    d={}
    for k,v in Uey().items():
        d[v['UEY']['Isolated']]=k
        d[v['UEY']['Simple Isolated']]=k
        d[v['UEY']['Initial']]=k
        d[v['UEY']['Simple Initial']]=k
        d[v['UEY']['Medial']]=k
        d[v['UEY']['Final']]=k
    return d



def Uly():
    uly={}
    for k,v in IPA_SCRIPTS.items():
        key=v['ULY']['sentence_start']
        key1=v['ULY']['other']
        if key in uly:
            uly[key]['IPA'].append(k)
            continue
        dd={}
        dd["IPA"]=[k]
        dd["UEY"]=v["UEY"]
        dd["UKY"]=v["UKY"]
        dd["UYY"] = v["UYY"]
        uly[key]= dd
        uly[key1] = dd
    return uly

def Uky():
    uky = {}
    for k, v in IPA_SCRIPTS.items():
        key = v['UKY']['sentence_start']
        key1 = v['UKY']['other']
        if key in uky:
            uky[key]['IPA'].append(k)
            continue
        dd = {}
        dd["IPA"] = [k]
        dd["UEY"] = v["UEY"]
        dd["ULY"] = v["ULY"]
        dd["UYY"] = v["UYY"]
        uky[key] = dd
        uky[key1] = dd
    return uky

def Uyy():
    uyy = {}
    for k, v in IPA_SCRIPTS.items():
        key = v['UYY']['sentence_start']
        key1 = v['UYY']['other']
        if key in uyy:
            uyy[key]['IPA'].append(k)
            continue
        dd = {}
        dd["IPA"] = [k]
        dd["UEY"] = v["UEY"]
        dd["ULY"] = v["ULY"]
        dd["UKY"] = v["UKY"]
        uyy[key] = dd
        uyy[key1] = dd
    return uyy


def deep_unicode_escape(obj):
    """递归处理所有字符串类型值"""
    if isinstance(obj, str):
        return ''.join(f'\\u{ord(c):04x}' for c in obj)
    elif isinstance(obj, MutableMapping):
        return {k: deep_unicode_escape(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [deep_unicode_escape(item) for item in obj]
    return obj

def print_escaped(data):
    """输出带Unicode转义的字典"""
    d={}
    for k,v in data.items():
        d[deep_unicode_escape(k)]=deep_unicode_escape(v)
    json_str = json.dumps(d, indent=2, ensure_ascii=True)
    print(json_str.replace('\\\\', '\\'))
# 输出\uXXXX
# print_escaped(Uey())
# print_escaped(UEY_latter_map())
# print_escaped(Uky())
# print_escaped(Uly())
# print_escaped(Uyy())

# 输出具体字母
# print(Uky())
