class Board:

    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("  |  ".join(self.board[i : i + 3]))
            if i < 6:
                print("-" * 15)

    def update_board(self, symbol, place):
        self.board[place - 1] = symbol

    def valid_move(self, place):
        return self.board[place - 1].isdigit()

    def clear_board(self):
        self.board = [i for i in range(1, 10)]
