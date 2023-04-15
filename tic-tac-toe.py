import random


# 1. Start with our introduction function
def intro():
    print("Welcome to my Tic-Tac-Toe Game!")


def get_player_letter():
    # Lets the player choose the letter they want to be
    # Return a list with the player's letter as the first item and the computer's letter as the second
    player_letter = ""
    while player_letter != "X" and player_letter != "O":
        print("Do you want to be X or O?")
        player_letter = input().upper()

    if player_letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def draw_board(board):
    # This function gets the board argument and uses that to draw the state of the game per time
    # The board parameter is the variable that keeps track of every play happening on the board
    # The board parameter is going to be a list with length 9 because our board has 9 spaces.

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def coin_toss():
    # Determine who goes first
    # Assume the computer is 0 and the player is 1
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


