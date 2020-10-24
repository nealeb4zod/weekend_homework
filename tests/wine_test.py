import unittest

from classes.wine import Wine


class TestWine(unittest.TestCase):
    def setUp(self):
        self.red_wine = Wine("House Red", 10.00, 10, 8, "red", "Australia")

    def test_wine_colour(self):
        self.assertEqual("red", self.red_wine.colour)

    def test_wine_country(self):
        self.assertEqual("Australia", self.red_wine.country)