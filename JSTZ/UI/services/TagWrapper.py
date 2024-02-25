class TagWrapper:
    tags = {
        "-": '<span class="extra-char">',
        "+": '<span class="missing-char">',
        "close": "</span>"
    }


    @classmethod
    def mk_html_tags(cls, string):
        result = []
        ptr = 0
        while ptr < len(string):
            if string[ptr] in cls.tags:
                result.append(cls.tags[string[ptr]])
                ptr += 2
                result.append(string[ptr])
                result.append(cls.tags["close"])
            else:
                result.append(string[ptr])
            ptr += 1
        return ''.join(map(str.strip, result))