from classes.stockitem import StockItem


class Drink(StockItem):
    def __init__(self, name, price, quantity, units):
        super().__init__(name, price, quantity)
        self.units = units
