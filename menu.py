from time import sleep

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

    def players_menu(self):
        print("Player1: ")
        player1 = Player()
        player1.choose_name()
        player1.choose_symbol()

        print("\nPlayer2: ")
        player2 = Player()
        while True:
            player2.choose_name()
            if player2.name != player1.name:
                break
            else:
                print("Player 2 can't have Player 1's name")

        while True:
            player2.choose_symbol()
            if player2.symbol != player1.symbol:
                break
            else:
                print("Player 2 can't have Player 1's symbol")

        return (player1, player2)

    def result_menu(self, player: str = None, draw: bool = False):
        if draw:
            print("Draw")
        else:
            print(f"{player} Wins")

        while True:
            choice = input("\n\nEnter:\n\t1. To Play Again\n\t2. To Quit\n\t\t: ")
            if choice == "1" or choice == "2":
                if choice == "1":
                    self.main_menu()
                elif choice == "2":
                    self.quit_menu()
                break
            print("Invalid Choice. ")
