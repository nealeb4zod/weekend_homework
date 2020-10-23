import unittest

from classes.venue import Venue


class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue_1 = Venue("Nakatomi Tower")

    def test_venue_name(self):
        self.assertEqual("Nakatomi Tower", self.venue_1.name)

    def test_venue_initial_takings_zero(self):
        self.assertEqual(0, self.venue_1.takings)