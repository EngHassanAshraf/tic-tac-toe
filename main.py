from time import sleep
from menu import Menu
from board import Board


def main_screen():
    choice = input(
        "\nWelcome to the Tik Tak Toe Game\nEnter:\n\t1. To Start\n\t2. To Quite\n\t\t: "
    )

    while choice != "1" and choice != "2":
        choice = input(
            "We don't understand your choice, please\nEnter:\n\t1. To Start\n\t2. To Quite\n\t\t: "
        )

    return choice


def player_move():
    move = input("Enter a place: ")
    return int(move)


def main():
    choice = main_screen()

    if choice == "1":
        board = Board()
        players = Menu().players_menu()
        # print(f"\n {player.name} Turn  \nAvailable Palces: \n")
        # board.display_board()
        # print()
        # selected_place = player_move()
        # if board.valid_move(selected_place):
        #     board.update_board(
        #         player.symbol,
        #         place=selected_place,
        #     )
        # else:
        #     print("invalid selection")

    elif choice == "2":
        print("\n\n\tHave a nice day, GoodBye\n\n")
        sleep(3)
        exit()


if __name__ == "__main__":
    main()
