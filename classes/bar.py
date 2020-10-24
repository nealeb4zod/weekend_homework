class Bar:
    def __init__(self, name, till, stock_list):
        self.name = name
        self.till = till
        self.stock_list = stock_list

    def check_item_in_stock_list(self, item):
        for stock_list_item in self.stock_list:
            return (False, True)[item.name == stock_list_item.name]

    def check_item_quantity(self, item):
        for stock_list_item in self.stock_list:
            return (False, True)[item.quantity <= stock_list_item.quantity]

    def reduce_item_quantity(self, item):
        for stock_list_item in self.stock_list:
            if item.name == stock_list_item.name:
                stock_list_item.quantity -= item.quantity

    def add_money_to_till(self, amount):
        self.till += amount

    def sell_item_to_customer(self, customer, item_to_sell):
        price = item_to_sell.price
        if (
            self.check_item_in_stock_list(item_to_sell)
            and self.check_item_quantity(item_to_sell)
            and customer.check_wallet_balance(price) == True
        ):
            self.reduce_item_quantity(item_to_sell)
            self.add_money_to_till(price)
            customer.remove_from_wallet(price)
