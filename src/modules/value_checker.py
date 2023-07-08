class ValueChecker:
    def is_non_negative_integer(self, value: int):
        if isinstance(value, int) and value >= 0:
            return True
        return False
    
    def is_non_empty_string(self, value:str):
        if isinstance(value, str) and value != '':
            return True
        return False