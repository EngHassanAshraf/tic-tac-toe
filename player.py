
class Player:

    def __init__(self):
        self.symbol = ""

    def validate_symbol(self, symbol:str):
        return symbol.isalpha() and len(symbol) == 1

    def choose_symbol(self):
        while True:
            symbol = input("Symbol: ")
            if self.validate_symbol(symbol):
                self.symbol = symbol
                break
            print('Invalid Symbole. Please use single "letter".')
