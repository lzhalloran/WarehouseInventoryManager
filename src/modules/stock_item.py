import value_checker

class StockItem:
    def __init__(self, identifier: int, product: int, location):
        if value_checker.is_non_negative_integer(identifier):
            self._identifier = identifier
        else:
            raise ValueError("Identifier must be a non-negative integer value")
        if value_checker.is_non_negative_integer(product):
            self._product = product
        else:
            raise ValueError("Product must be a non-negative integer value")
        self.location = location
        
    @property
    def identifier(self):
        return self._identifier
    
    @property
    def product(self):
        return self._product
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if value_checker.is_non_empty_string(value[0]) and value_checker.is_non_negative_integer(value[1]) and value_checker.is_non_negative_integer(value[2]):
            self._location = value
        else:
            raise ValueError("Location must have following format: [Roomname (non-empty string), Row (non-negative integer), Height (non-negative integer)]")