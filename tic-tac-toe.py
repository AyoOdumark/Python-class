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


def update_board(move, board, letter):
    # For example, if the player's move is at position 5. Our update_board is going to set board[5] = player_letter
    board[move] = letter


def is_space_free(board, move):
    # Return True if the passed move is free on the board
    return board[move] == " "


def get_player_move(board):
    # Prompt the player to make a move
    # check if it is a legit move. Check if the space is empty or free
    move = " "
    while move not in "0 1 2 3 4 5 6 7 8".split() or not is_space_free(board, int(move)):
        print("What is your next move? (0-8)")
        move = input()
    return int(move)


def is_winner(board, letter):
    # Given a board and player's letter, this function returns True if that player has won.
    if board[0] == letter and board[1] == letter and board[2] == letter:  # Checking for the first row
        return True
    elif board[3] == letter and board[4] == letter and board[5] == letter:  # Checking for the second row
        return True
    elif board[6] == letter and board[7] == letter and board[8] == letter:  # Checking for the third row
        return True
    elif board[0] == letter and board[3] == letter and board[6] == letter:  # Checking for the first column
        return True
    elif board[1] == letter and board[4] == letter and board[7] == letter:  # Checking for the second column
        return True
    elif board[2] == letter and board[5] == letter and board[8] == letter:  # Checking for the third column
        return True
    elif board[0] == letter and board[4] == letter and board[8] == letter:  # Checking for first diagonal
        return True
    elif board[2] == letter and board[4] == letter and board[6] == letter:  # Checking for second diagonal
        return True
    else:
        return False


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise, return False.
    for i in range(9):
        if is_space_free(board, i):
            return False
    return True


def get_board_copy(board):
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def choose_random_move_from_list(board, moves):
    # Returns a valid move from the passed list on the board
    possible_moves = []
    for i in moves:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move
    if computer_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    # Here is the algorithm for our Tic-Tac-Toe AI:
    # 1. Check if we can win in the next move
    for i in range(9):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            update_board(i, board_copy, computer_letter)
            if is_winner(board_copy, computer_letter):
                return i

    # 2. Check if the player could win on their next move and block them
    for i in range(9):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            update_board(i, board_copy, player_letter)
            if is_winner(board_copy, player_letter):
                return i

    board_copy = get_board_copy(board)
    # 3. Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board_copy, [0, 2, 6, 8])
    if move != None:
        return move

    # 4. Try to take the center, if it is free.
    if is_space_free(board, 4):
        return 4

    # 5. Move on one of the sides
    return choose_random_move_from_list(board, [1, 3, 5, 7])


# Game loop
while True:
    # Reset the board
    game_board = [" "] * 9
    intro()
    player_letter, computer_letter = get_player_letter()
    turn = coin_toss()
    print(f"The {turn} will go first.")
    game_is_playing = True  # Game state variable. To keep track if the game is in session or the game has ended

    while game_is_playing:
        if turn == "player":
            # Player's turn
            draw_board(game_board)
            move = get_player_move(game_board)
            update_board(move, game_board, player_letter)

            if is_winner(game_board, player_letter):
                draw_board(game_board)
                print("Hooray! You have won the game!")
                game_is_playing = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"

        else:
            # Computer's turn
            move = computer_move(game_board, computer_letter)
            update_board(move, game_board, computer_letter)

            if is_winner(game_board, computer_letter):
                draw_board(game_board)
                print("The computer has beaten you! You lose.")
                game_is_playing = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break



