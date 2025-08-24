from os import system
from board import Board
from player import Player
from menu import Menu


class Game:

    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
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

    def setup_players(self):
        for number, player in enumerate(self.players, 1):
            print(f"Player {number}")
            print("-" * 20)
            player.choose_name()
            player.choose_symbol()
            system("cls")

    def play(self):
        pass

    def play_turn(self):
        pass

    def check_win(self):
        pass

    def check_draw(self):
        pass

    def restart_game(self):
        pass

    def quit_game(self):
        pass


game = Game()
game.start_game()
