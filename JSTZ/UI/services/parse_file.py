import re

class StudentTranslationParser:
    
    newline_pattern    = re.compile(r"\n+")
    numeration_pattern = re.compile(r"[\)\.．]")
    
    @classmethod
    def parse(cls, text) -> dict:
        """Assume the first string is always meta"""
        
        data = cls.newline_pattern.split(text)
        data = map(str.strip, data[1:])
        data = [c for c in data if c.strip()]
        
        data = map(lambda c: cls.numeration_pattern.split(c, maxsplit=1), data)
        
        data = map(lambda c: (int(c[0]), c[1]), data)
        
        result = dict()
        for i, sent in data:
            result[i] = result.get(i, []) + [sent]
        
        return result
    



# def parse_file(data: str):
#     """Assume file is already read"""
#     result = {}

#     data = data.split("\n")

#     for c in data:
#         lesson, content = c.split(")")
#         lesson = int(lesson)
#         result[lesson] = content

#     return result