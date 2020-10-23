import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest
from classes.venue import Venue


class TestRoom(unittest.TestCase):
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

        self.venue_1 = Venue("Nakatomi Tower")

        self.room_1 = Room("The Lobby", 5, self.venue_1)

    def test_room_name(self):
        self.assertEqual("The Lobby", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_room_bar_tab(self):
        self.assertEqual(0, self.room_1.bar_tab)

    def test_room_can_add_guest(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.assertEqual(2, len(self.room_1.guest_list))
        self.assertEqual(2, len(self.room_1.playlist))

    def test_room_can_remove_guest(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.assertEqual(2, len(self.room_1.guest_list))
        self.assertEqual(2, len(self.room_1.playlist))
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))
        self.assertEqual(1, len(self.room_1.playlist))

    def test_room_cannot_add_guest__over_capacity(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.add_guest_to_room(self.guest_4)
        self.room_1.add_guest_to_room(self.guest_5)
        self.room_1.add_guest_to_room(self.guest_6)
        self.assertEqual(5, len(self.room_1.guest_list))

    def test_add_song_to_room_playlist(self):
        self.room_1.add_song_to_room_playlist(self.song_7)
        self.assertEqual(1, len(self.room_1.playlist))

    def test_remove_song_from_room_playlist(self):
        self.room_1.add_song_to_room_playlist(self.song_7)
        self.assertEqual(1, len(self.room_1.playlist))
        self.room_1.remove_song_from_playlist(self.song_7)
        self.assertEqual(0, len(self.room_1.playlist))

    def test_adding_guest_to_room_increases_venue_takings(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(10, self.venue_1.takings)

    def test_check_song_on_playlist__true(self):
        self.room_1.add_song_to_room_playlist(self.song_1)
        self.assertTrue(self.room_1.check_song(self.song_1))

    def test_check_song_on_playlist__false(self):
        self.room_1.add_song_to_room_playlist(self.song_1)
        self.assertFalse(self.room_1.check_song(self.song_2))

    def test_favourite_song_makes_guest_cheer(self):
        self.room_1.add_guest_to_room(self.guest_3)
        self.assertEqual("WHERE ARE MY DETONATORS!", self.room_1.play_song(self.song_3))
