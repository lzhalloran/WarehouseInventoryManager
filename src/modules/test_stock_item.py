import pytest
from stock_item import StockItem


class TestStockItem:
    valid_test_data = [
        {'identifier': 123456789,
            'product': 12948,
            'location': ["Room1", 4, 1]},
        {'identifier': 2,
            'product': 1,
            'location': ["A", 1, 1]}
    ]

    invalid_test_data = [
        {'identifier': '123456789',
            'product': 12948.0,
            'location': [1, 4.0, "1"]},
        {'identifier': [345, 456],
            'product':1654,
            'location':["1", 2, 7]},
        {'identifier': 654,
            'product': "asdf",
            'location': ["AB", 5, 100]},
        {'identifier': 123456789,
            'product': 12948,
            'location': [65, 4, 1]},
        {'identifier': 123456789,
            'product': 12948,
            'location': [1, 4.0, 1]},
        {'identifier': 123456789,
            'product': 12948,
            'location': ["Room6", 4, "5"]},
        {'identifier': 123456789,
            'product': 12948,
            'location': ["", 4, 5]},
        {'identifier': -1,
            'product': 23904243,
            'location': ["Room1", 2, 0]},
        {'identifier': 1,
            'product': -23904243,
            'location': ["Room1", 2, 0]},
        {'identifier': 1,
            'product': 23904243,
            'location': ["Room1", -2, 0]},
        {'identifier': 1,
            'product': 23904243,
            'location': ["Room1", 2, -1]}
    ]

    @pytest.fixture(scope='session', params=valid_test_data)
    def create_valid_stock_item(self, request):
        return StockItem(request.param.get('identifier'),
                         request.param.get('product'),
                         request.param.get('location'))

    @pytest.mark.parametrize('data', valid_test_data)
    def test_stock_item_initial_value(self, data):
        item = StockItem(data.get('identifier'), data.get(
            'product'), data.get('location'))
        assert [item.identifier, item.product, item.location] == [
            data.get('identifier'), data.get('product'), data.get('location')]

    def test_stock_item_no_value(self):
        with pytest.raises(Exception):
            item = StockItem()

    @pytest.mark.parametrize('invalid_data', invalid_test_data)
    def test_stock_item_invalid_arguments(self, invalid_data):
        with pytest.raises(ValueError):
            item = StockItem(invalid_data.get('identifier'), 
                             invalid_data.get('product'), 
                             invalid_data.get('location'))


    def test_stock_item_change_location(self, create_valid_stock_item):
        new_location = ["Room5", 16, 4]
        create_valid_stock_item.location = new_location
        assert create_valid_stock_item.location == new_location
    
    def test_stock_item_change_identifier(self, create_valid_stock_item):
        with pytest.raises(AttributeError):
            create_valid_stock_item.identifier = 654

    def test_stock_item_change_product(self, create_valid_stock_item):
        with pytest.raises(AttributeError):
            create_valid_stock_item.product = 321