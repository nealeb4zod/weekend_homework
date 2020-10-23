import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest


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
        self.guest_1 = Guest("John McLean", 39, self.song_1, 100.00)
        self.guest_2 = Guest("Al Powell", 43, self.song_2, 50.00)
        self.guest_3 = Guest("Hans Gruber", 47, self.song_3, 10000.00)
        self.guest_4 = Guest("Karl Vreski", 35, self.song_4, 0.00)
        self.guest_5 = Guest("Argyle", 30, self.song_5, 20.00)
        self.guest_6 = Guest("Mr Takagi", 35, self.song_6, 100000.00)

        self.room_1 = Room("The Lobby", 5)

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

    def test_room_playlist(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.assertEqual(2, len(self.room_1.playlist))

    def test_room_can_remove_guest(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.assertEqual(2, len(self.room_1.guest_list))
        self.assertEqual(2, len(self.room_1.playlist))
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))
        self.assertEqual(1, len(self.room_1.playlist))