import value_checker

class StockItem:
    def __init__(self, identifier: int, product: int, location):
        if value_checker.is_non_negative_integer(identifier):
            self.identifier = identifier
        else:
            raise ValueError("Identifier must be a non-negative integer value")
        if value_checker.is_non_negative_integer(product):
            self.product = product
        else:
            raise ValueError("Product must be a non-negative integer value")
        if value_checker.is_non_empty_string(location[0]) and value_checker.is_non_negative_integer(location[1]) and value_checker.is_non_negative_integer(location[2]):
            self.location = location
        else:
            raise ValueError("Location must have following format: [Roomname (non-empty string), Row (non-negative integer), Height (non-negative integer)]")