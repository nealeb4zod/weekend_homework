import unittest

from classes.bar import Bar
from classes.beer import Beer
from classes.wine import Wine


class TestBar(unittest.TestCase):
    def setUp(self):
        self.tennents = Beer("Tennents", 2.50, 50, 2, "Lager")
        self.house_red = Wine("House Red", 10.00, 10, 8, "red", "Australia")
        self.house_white = Wine("House Red", 10.00, 10, 8, "white", "New Zealand")

        stock = [self.tennents, self.house_red, self.house_white]

        self.main_bar = Bar("Main Bar", 0, stock)

    def test_bar_name(self):
        self.assertEqual("Main Bar", self.main_bar.name)

    def test_bar_till(self):
        self.assertEqual(0, self.main_bar.till)

    def test_bar_stock_list(self):
        self.assertEqual(3, len(self.main_bar.stock_list))