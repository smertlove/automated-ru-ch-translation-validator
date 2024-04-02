def load_rows(filename, row_dtype=set):
    
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
    
    data = data.strip()
    data = data.split("\n")
    data = list(map(lambda c: c.split("\t"), data))
    data = list(map(row_dtype, data))
    
    return data
    