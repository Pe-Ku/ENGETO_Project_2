"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Peter Kubovcik
email: peter.kubovcik@gmail.com
discord: Peter K.
"""

import os

separator = '=' * 44
empty_game_board = {7: ' ', 8: ' ', 9: ' ',
                    4: ' ', 5: ' ', 6: ' ',
                    1: ' ', 2: ' ', 3: ' '}


def game_tic_tac_toe():
    game_rules()
    counter = 0
    game_board = initialize_game_board(empty_game_board)
    while True:
        os.system("cls")
        print_board(game_board)
        player = player_switch(counter)
        while True:
            answer = player_input(player)
            if check_answer(answer, player, game_board) is True:
                break
        counter += 1
        if check_win(game_board) is True:
            os.system("cls")
            print_board(game_board)
            winner_message(player)
            break
        elif check_draw(game_board) is True:
            os.system("cls")
            print_board(game_board)
            draw_message()
            break
    next_game()


def game_rules():
    print(
        "Welcome to Tic Tac Toe",
        separator,
        "Game rules".upper(),
        "Each player can place one mark (or stone)",
        "per turn on the 3x3 grid. The WINNER is",
        "who succeeds in placing three of their",
        "marks in a:",
        "* horizontal,",
        "* vertical or",
        "* diagonal row",
        separator,
        "Play grid numbering is equal to numeric pad",
        separator,
        sep="\n"
    )
    input("Press ENTER to start the game")


def initialize_game_board(empty_game_board):
    game_board = dict.fromkeys(empty_game_board, ' ')
    return game_board


def print_board(game_board):
    print(game_board[7] + '|' + game_board[8] + '|' + game_board[9],
          '-+-+-',
          game_board[4] + '|' + game_board[5] + '|' + game_board[6],
          '-+-+-',
          game_board[1] + '|' + game_board[2] + '|' + game_board[3],
          sep="\n")


def player_input(player):
    while True:
        player_position = input(f"Player {player} | Please enter your move number: ")
        if (
                player_position.isnumeric() and
                int(player_position) in range(1, 10)
        ):
            return player_position
        else:
            print("Wrong input, try again!")


def check_answer(answer, player, game_board):
    if game_board[int(answer)] == ' ':
        game_board[int(answer)] = player
        return True
    else:
        print("Position is taken, try other!")
        return False


def player_switch(counter):
    if counter % 2 == 0:
        return 'X'
    else:
        return 'O'


def check_win(game_board):
    """
    Checks possible winning options.
    :param game_board:
    :return:
    """
    if (
            game_board[1] == game_board[2] == game_board[3] != ' ' or
            game_board[4] == game_board[5] == game_board[6] != ' ' or
            game_board[7] == game_board[8] == game_board[9] != ' ' or
            game_board[1] == game_board[4] == game_board[7] != ' ' or
            game_board[2] == game_board[5] == game_board[8] != ' ' or
            game_board[3] == game_board[6] == game_board[9] != ' ' or
            game_board[1] == game_board[5] == game_board[9] != ' ' or
            game_board[3] == game_board[5] == game_board[7] != ' '
    ):
        return True


def winner_message(player):
    print(f"Congratulations, the player {player} WON!")


def check_draw(game_board):
    if all(game_board[value] != ' ' for value in game_board):
        return True


def draw_message():
    print(f"Draw!")


def next_game():
    next_round = input("Another round? [y / n].")
    if next_round == 'y':
        return game_tic_tac_toe()
    else:
        exit()


game_tic_tac_toe()
