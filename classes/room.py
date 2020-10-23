class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.playlist = []
        self.guest_list = []
        self.bar_tab = 0

    def add_guest_to_room(self, guest):
        self.guest_list.append(guest)
        self.playlist.append(guest.favourite_song)

    def remove_guest_from_room(self, guest):
        guest_index = self.guest_list.index(guest)
        self.guest_list.pop(guest_index)
        song_index = self.playlist.index(guest.favourite_song)
        self.playlist.pop(song_index)
        
