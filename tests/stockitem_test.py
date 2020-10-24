import unittest
from classes.stockitem import StockItem


class TestStockItem(unittest.TestCase):
    def setUp(self):
        self.stockitem = StockItem("Beer", 5.00, 10)

    def test_stockitem_name(self):
        self.assertEqual("Beer", self.stockitem.name)

    def test_stockitem_price(self):
        self.assertEqual(5.00, self.stockitem.price)

    def test_stockitem_quantity(self):
        self.assertEqual(10, self.stockitem.quantity)

