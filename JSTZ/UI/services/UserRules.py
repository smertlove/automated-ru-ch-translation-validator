#  БЛОК ПОЛЬЗОВАТЕЛЬСКИХ ФУНКЦИЙ  #


import pypinyin

def mk_regexp_piece(elems: list):
    return f"({'|'.join(elems)})"

def _get_synonyms(word: str):
    synonym_groups = [
    {"你",  "您", "你们"},
    {"对了", "是的", "对", "是"},
    {"汉语",  "中文"},
    {"不客气",  "不谢"},
    {"姓什么",  "贵姓"}
    ]
    for group in synonym_groups:
        if word in group:
            return [c for c in group]
    return [word]

def get_synonyms(word: str):
    return mk_regexp_piece(_get_synonyms(word))

def _get_pinyin(word: str):
    pinyin=[]
    for elem in pypinyin.pinyin(word):
        pinyin.append(elem[0])
    return [word] + [''.join(pinyin)]

def get_pinyin(word: str):
    return mk_regexp_piece(_get_pinyin(word))


RULES = {"s": get_synonyms, "p": get_pinyin}

def zhengzaine(string: str) -> str:
    a1 = f"正在{string}呢"
    a2 = f"正在{string}"
    a3 = f"在{string}呢"
    a4 = f"在{string}"
    return f"({a1}|{a2}|{a3}|{a4})"

RULES["正在"] = zhengzaine



