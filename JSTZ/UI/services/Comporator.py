from difflib import Differ
import exrex


class ChineseRegexpComporator:

    @classmethod
    def get_all_variants(cls, regexp: str):
        return tuple(exrex.generate(regexp))

    @classmethod
    def compare(cls, string: str, regexp: str):
        string = ''.join(string.split())

        regexps = cls.get_all_variants(regexp)
        results = []

        for regexp in regexps:
            dif = Differ().compare(string, regexp)
            results.append(tuple(dif))

        results.sort(key=lambda c: sum([1 for cc in c if "-" in cc]) + sum([1 for cc in c if "+" in cc]))
        return results[0]



