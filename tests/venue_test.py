import unittest

from classes.venue import Venue
from classes.beer import Beer
from classes.wine import Wine
from classes.bar import Bar


class TestVenue(unittest.TestCase):
    def setUp(self):
        self.tennents = Beer("Tennents", 2.50, 50, 2, "Lager")
        self.house_red = Wine("House Red", 10.00, 10, 8, "red", "Australia")
        self.house_white = Wine("House Red", 10.00, 10, 8, "white", "New Zealand")

        stock = [self.tennents, self.house_red, self.house_white]

        self.main_bar = Bar("Main Bar", 0, stock)
        self.venue_1 = Venue("Nakatomi Tower", self.main_bar)

    def test_venue_name(self):
        self.assertEqual("Nakatomi Tower", self.venue_1.name)

    def test_venue_entry_fee(self):
        self.assertEqual(10, self.venue_1.entry_fee)

    def test_venue_initial_takings_zero(self):
        self.assertEqual(0, self.venue_1.takings)

    def test_add_to_venue_takings(self):
        self.venue_1.add_to_takings(100)
        self.assertEqual(100, self.venue_1.takings)