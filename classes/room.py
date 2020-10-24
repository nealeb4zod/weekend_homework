class Room:
    def __init__(self, name, capacity, venue):
        self.name = name
        self.capacity = capacity
        self.playlist = []
        self.guest_list = []
        self.venue = venue

    def add_guest_to_room(self, guest):
        if len(self.guest_list) < self.capacity:
            guest.remove_from_wallet(self.venue.entry_fee)
            self.venue.add_to_takings(self.venue.entry_fee)
            self.guest_list.append(guest)
            self.add_song_to_room_playlist(guest.favourite_song)

    def remove_guest_from_room(self, guest):
        guest_index = self.guest_list.index(guest)
        self.guest_list.pop(guest_index)
        self.remove_song_from_playlist(guest.favourite_song)

    def add_song_to_room_playlist(self, song):
        if self.check_song(song) == False:
            self.playlist.append(song)

    def remove_song_from_playlist(self, song):
        if self.check_song(song):
            song_index = self.playlist.index(song)
            self.playlist.pop(song_index)

    def check_song(self, song):
        return (False, True)[song in self.playlist]

    def play_song(self, song):
        if self.check_song(song) == True:
            for guest in self.guest_list:
                if song == guest.favourite_song:
                    self.remove_song_from_playlist(song)
                    return guest.cheer
        self.remove_song_from_playlist(song)
