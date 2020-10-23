class Room:
    def __init__(self, name, capacity, venue):
        self.name = name
        self.capacity = capacity
        self.playlist = []
        self.guest_list = []
        self.bar_tab = 0
        self.venue = venue

    def add_guest_to_room(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
            self.add_song_to_room_playlist(guest.favourite_song)
            self.venue.add_to_takings(self.venue.entry_fee)

    def remove_guest_from_room(self, guest):
        guest_index = self.guest_list.index(guest)
        self.guest_list.pop(guest_index)
        self.remove_song_from_playlist(guest.favourite_song)

    def add_song_to_room_playlist(self, song):
        self.playlist.append(song)

    def remove_song_from_playlist(self, song):
        song_index = self.playlist.index(song)
        self.playlist.pop(song_index)