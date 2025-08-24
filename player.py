class Player:

    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid Name. Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input("Symbol: ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol
                break
            print('Invalid Symbole. Please use single "letter".')
