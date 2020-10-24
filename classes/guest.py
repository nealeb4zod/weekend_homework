class Guest:
    def __init__(self, name, age, favourite_song, wallet, cheer):
        self.name = name
        self.age = age
        self.favourite_song = favourite_song
        self.wallet = wallet
        self.cheer = cheer

    def check_wallet_balance(self, amount):
        if amount <= self.wallet:
            return True
        else:
            return False

    def remove_from_wallet(self, amount):
        if self.check_wallet_balance(amount) == True:
            self.wallet -= amount
            return True
        else:
            return False