class Venue:
    def __init__(self, name, bar):
        self.name = name
        self.takings = 0
        self.entry_fee = 10
        self.bar = bar

    def add_to_takings(self, amount):
        self.takings += amount