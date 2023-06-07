
def parse_file(data: str):
    """Assume file is already read"""
    result = {}

    data = data.split("\n")

    for c in data:
        lesson, content = c.split(")")
        lesson = int(lesson)
        result[lesson] = content

    return result