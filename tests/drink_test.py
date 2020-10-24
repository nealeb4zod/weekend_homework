import unittest
from classes.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 5.00, 10, 2)

    def test_drink_units(self):
        self.assertEqual(2, self.drink.units)
