def is_non_negative_integer(value: int):
    if isinstance(value, int) and value >= 0:
        return True
    return False

def is_non_empty_string(value:str):
    if isinstance(value, str) and value != '':
        return True
    return False