class Venue:
    def __init__(self, name):
        self.name = name
        self.takings = 0
        self.entry_fee = 10

    def add_to_takings(self, amount):
        self.takings += amount