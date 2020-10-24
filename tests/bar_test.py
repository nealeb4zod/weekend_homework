import unittest

from classes.bar import Bar
from classes.beer import Beer
from classes.wine import Wine
from classes.song import Song
from classes.guest import Guest


class TestBar(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Run-D.M.C.", "Christmas in Hollis")
        self.song_2 = Song("Skeletons", "Stevie Wonder")
        self.song_3 = Song("Beethoven", "Ode to Joy")
        self.song_4 = Song("Let It Snow! Let It Snow! Let It Snow!", "Vaughn Monroe")
        self.song_5 = Song("Jingle Bells", "Bruce Willis")
        self.song_6 = Song(
            "Brandenburg Concerto No. 3 In G Major, (Allegro Moderato)", "Bach"
        )
        self.song_7 = Song("Winter Wonderland", " Felix Bernard and Richard B. Smith")

        self.guest_1 = Guest("John McLean", 39, self.song_1, 100.00, "Yippee-ky-ay!!")
        self.guest_2 = Guest(
            "Al Powell",
            43,
            self.song_2,
            50.00,
            "Now means now goddammit!, I'm under automatic rifle fire at Nakatomi, I need backup assistance now! NOW, GODDAMMIT, NOW!",
        )
        self.guest_3 = Guest(
            "Hans Gruber", 47, self.song_3, 10000.00, "WHERE ARE MY DETONATORS!"
        )
        self.guest_4 = Guest(
            "Karl Vreski", 35, self.song_4, 0.00, "No one kills him but me!"
        )
        self.guest_5 = Guest(
            "Argyle", 30, self.song_5, 20.00, "This *is* Christmas music!"
        )
        self.guest_6 = Guest(
            "Mr Takagi",
            35,
            self.song_6,
            100000.00,
            "I guess you'll just have to kill me then!",
        )
        self.tennents = Beer("Tennents", 2.50, 50, 2, "Lager")
        self.house_red = Wine("House Red", 10.00, 10, 8, "red", "Australia")
        self.house_white = Wine("House White", 10.00, 10, 8, "white", "New Zealand")

        self.stella = Beer("Stella Artois", 5.00, 10, 2.5, "Lager")

        stock = [self.tennents, self.house_red, self.house_white]

        self.main_bar = Bar("Main Bar", 0, stock)

    def test_bar_name(self):
        self.assertEqual("Main Bar", self.main_bar.name)

    def test_bar_till(self):
        self.assertEqual(0, self.main_bar.till)

    def test_bar_stock_list(self):
        self.assertEqual(3, len(self.main_bar.stock_list))

    def test_add_money_to_till(self):
        self.main_bar.add_money_to_till(10)
        self.assertEqual(10, self.main_bar.till)

    def test_check_item_in_list__in_list(self):
        result = self.main_bar.check_item_in_stock_list(self.tennents)
        self.assertEqual(True, result)

    def test_check_item_in_list__not_in_list(self):
        result = self.main_bar.check_item_in_stock_list(self.stella)
        self.assertEqual(False, result)

    def test_check_item_quantity__exact_match(self):
        result = self.main_bar.check_item_quantity(self.tennents)
        self.assertEqual(True, result)

    def test_check_item_quantity__less_than_quantity(self):
        self.tennents = Beer("Tennents", 2.50, 49, 2, "Lager")
        result = self.main_bar.check_item_quantity(self.tennents)
        self.assertEqual(True, result)

    def test_check_item_quantity__more_than_quantity(self):
        self.tennents = Beer("Tennents", 2.50, 51, 2, "Lager")
        result = self.main_bar.check_item_quantity(self.tennents)
        self.assertEqual(False, result)

    def test_reduce_item_quantity(self):
        house_red_single = Wine("House Red", 10.00, 1, 8, "red", "Australia")
        self.main_bar.reduce_item_quantity(house_red_single)
        self.assertEqual(9, self.house_red.quantity)

    def test_sell_item_to_customer(self):
        tennents_single = Beer("Tennents", 2.50, 1, 2, "Lager")
        self.main_bar.sell_item_to_customer(self.guest_1, tennents_single)
        self.assertEqual(49, self.tennents.quantity)
        self.assertEqual(2.50, self.main_bar.till)
        self.assertEqual(97.50, self.guest_1.wallet)
