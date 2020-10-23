import unittest

from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Run-D.M.C.", "Christmas in Hollis")
        self.song_2 = Song("Skeletons", "Stevie Wonder")
        self.song_3 = Song("Beethoven", "Ode to Joy")
        self.song_4 = Song("Let It Snow! Let It Snow! Let It Snow!", "Vaughn Monroe")

    def test_song_artist(self):
        self.assertEqual("Run-D.M.C.", self.song_1.artist)

    def test_song_title(self):
        self.assertEqual("Christmas in Hollis", self.song_1.title)