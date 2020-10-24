from classes.drink import Drink


class Wine(Drink):
    def __init__(self, name, price, quantity, units, colour, country):
        super().__init__(name, price, quantity, units)
        self.colour = colour
        self.country = country