from classes.drink import Drink


class Beer(Drink):
    def __init__(self, name, price, quantity, units, type):
        super().__init__(name, price, quantity, units)
        self.type = type