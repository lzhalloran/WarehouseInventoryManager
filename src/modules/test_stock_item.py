import pytest
from stock_item import StockItem

class TestStockItem:
    def test_stock_item_initial_value(self):
        identifier = 123456789
        product = 12054
        location = ["Room1", 4, 1]

        item = StockItem(identifier, product, location)
        assert [item.identifier, item.product, item.location] == [identifier, product, location]
    
    def test_stock_item_no_value(self):
        with pytest.raises(Exception) as error_info:
            item = StockItem()