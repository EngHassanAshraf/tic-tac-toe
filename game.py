from os import system
from board import Board
from player import Player
from menu import Menu


class Game:

    def __init__(self):
        self.players = [Player(), Player()]
        self.board_instance = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.main_menu()
        system("cls")
        if choice == 1:
            self.setup_players()
            self.play()
        else:
            self.quit_game()

    def restart_game(self):
        self.board_instance.clear_board()
        self.current_player_index = 0
        self.play()

    def setup_players(self):
        self.menu.players_menu(self.players)

    def play(self):
        while True:
            self.play_turn()
            system("cls")
            if self.check_win(): 
                print(f"\n\tPlayer {self.players[1 - self.current_player_index].symbol} Win")
                self.board_instance.display_board()
                break
            if self.check_draw():
                print(f"Draw")
                self.board_instance.display_board()
                break

        choice = self.menu.result_menu()
        if choice == 1:
            self.restart_game()
        elif choice == 2:
            self.quit_game()

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board_instance.display_board()
        print(f"Player {self.current_player_index+1}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell [1:9]: "))
                if 1 <= cell_choice <= 9 and self.board_instance.valid_move(cell_choice):
                    self.board_instance.update_board(player.symbol, place=cell_choice)
                    break
                else:
                    print("\n\tInvalid move,")
            except ValueError:
                print("\n\tPlease enter a number between 1 and 9.")
                
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        wins = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for win_cond in wins:
            if self.board_instance.board[win_cond[0]] == self.board_instance.board[win_cond[1]] == self.board_instance.board[win_cond[2]]:
                return True
        return False

        # if self.board_instance.board[0] == self.board_instance.board[1] == self.board_instance.board[2]:
        #     return True
        # if self.board_instance.board[3] == self.board_instance.board[4] == self.board_instance.board[5]:
        #     return True
        # if self.board_instance.board[6] == self.board_instance.board[7] == self.board_instance.board[8]:
        #     return True
        
        # if self.board_instance.board[0] == self.board_instance.board[3] == self.board_instance.board[6]:
        #     return True
        # if self.board_instance.board[1] == self.board_instance.board[4] == self.board_instance.board[7]:
        #     return True
        # if self.board_instance.board[2] == self.board_instance.board[5] == self.board_instance.board[8]:
        #     return True

        # if self.board_instance.board[0] == self.board_instance.board[4] == self.board_instance.board[8]:
        #     return True
        # if self.board_instance.board[2] == self.board_instance.board[4] == self.board_instance.board[6]:
        #     return True

        # return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board_instance.board)

    def quit_game(self):
        self.menu.quit_menu()


game = Game()
game.start_game()
