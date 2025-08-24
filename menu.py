from time import sleep
from os import system

from player import Player


class Menu:

    def main_menu(self):
        print("\nWelcome to the Tik Tak Toe Game")
        while True:
            choice = int(input("\nChoose:\n\t1. Start\n\t2. Quit\n\t: "))
            if choice == 1 or choice == 2:
                return choice
            else:
                print("\n\t\tInvalid Choice.")

    def quit_menu(self):
        print("\n\n\tHave a nice day, GoodBye\n\n")
        sleep(3)
        exit()

    def players_menu(self, players: list[Player]):
        for number, player in enumerate(players, 1):
            print(f"Player {number}")
            print("-" * 20)
            player.choose_symbol()
            system("cls")

    def result_menu(self):
        while True:
            choice = int(input("\n\nEnter:\n\t1. Play Again\n\t2. Quit\n\t\t: "))
            if choice == 1 or choice == 2:
                return choice
            print("\n\tInvalid Choice.")
