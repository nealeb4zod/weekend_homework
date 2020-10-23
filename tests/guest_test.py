import unittest

from classes.guest import Guest
from classes.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        song_1 = Song("Run-D.M.C.", "Christmas in Hollis")
        song_2 = Song("Skeletons", "Stevie Wonder")
        song_3 = Song("Beethoven", "Ode to Joy")
        song_4 = Song("Let It Snow! Let It Snow! Let It Snow!", "Vaughn Monroe")
        self.guest_1 = Guest("John McLean", 39, song_1, 100.00, "Yippee-ky-ay!!")
        self.guest_2 = Guest(
            "Al Powell",
            43,
            song_2,
            50.00,
            "Now means now goddammit!, I'm under automatic rifle fire at Nakatomi, I need backup assistance now! NOW, GODDAMMIT, NOW!",
        )
        self.guest_3 = Guest(
            "Hans Gruber", 47, song_3, 10000.00, "WHERE ARE MY DETONATORS!"
        )
        self.guest_4 = Guest(
            "Karl Vreski", 35, song_4, 0.00, "No one kills him but me!"
        )

    def test_guest_name(self):
        self.assertEqual("John McLean", self.guest_1.name)

    def test_guest_age(self):
        self.assertEqual(39, self.guest_1.age)

    def test_guest_favourite_song(self):
        self.assertEqual("Run-D.M.C.", self.guest_1.favourite_song.artist)
        self.assertEqual("Christmas in Hollis", self.guest_1.favourite_song.title)

    def test_guest_cheer(self):
        self.assertEqual("No one kills him but me!", self.guest_4.cheer)

    def test_guest_wallet(self):
        self.assertEqual(100, self.guest_1.wallet)