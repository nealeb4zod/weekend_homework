import unittest

from classes.beer import Beer


class TestBeer(unittest.TestCase):
    def setUp(self):
        self.beer = Beer("Sierra Nevada", 5.00, 10, 2, "IPA")

    def test_beer_type(self):
        self.assertEqual("IPA", self.beer.type)