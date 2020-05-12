# Game Board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# if Game is Still Going
game_still_going = True

# Who Win? or Tie?
winner = None

# Whose Turn it is
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" + " + " + "-" + " + " + "-")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" + " + " + "-" + " + " + "-")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play Game of Tic Tac Toe
def play_game():

    # Display Initial Board
    display_board()

    # While the Game is Still Going
    while game_still_going:

        # Handel a Single turn or Arbitrary Player
        handle_turn(current_player)

        # Check if the Game is Ended
        check_if_game_over()

        # Flip to the other Player
        flip_player()

    # The Game Is Ended
    if winner == "X" or winner == "O":
        print("Hey, " + winner + " It's Your Game, You are Won the Game.")
    elif winner == None:
        print("Hey, X and O Sorry It's Tie, Try Again.")


# Handel a Single turn or Arbitrary Player
def handle_turn(current_player):
    print(current_player + "'s Turn.")
    position = input("Enter a Position for " + current_player + " between 1-9 : ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Position, Enter a Valid Position for " + current_player + " between 1-9 : ")

        position = int(position) - 1

        if board[position] == " ":
            valid = True
        else:
            print("You Can't Go Again There.")

    board[position] = current_player

    display_board()


def check_if_game_over():
    check_for_win()
    check_if_tie()


def check_for_win():
    # Set Global Variable
    global winner

    # check row
    row_winner = check_row()
    # check columns
    columns_winner = check_columns()
    # check diagonal
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_row():
    # Set Global Variable
    global game_still_going

    # Check for Row Match
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "

    # if Any Row has a Match, flag that there is Win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the Winner "X" 0r "O"
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Set Global Variable
    global game_still_going

    # Check for Columns Match
    columns_1 = board[0] == board[3] == board[6] != " "
    columns_2 = board[1] == board[4] == board[7] != " "
    columns_3 = board[2] == board[5] == board[8] != " "

    # if Any Columns has a Match, flag that there is Win
    if columns_1 or columns_2 or columns_3:
        game_still_going = False

    # Return the Winner "X" 0r "O"
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return


def check_diagonal():
    # Set Global Variable
    global game_still_going

    # Check for Diagonal Match
    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[2] == board[4] == board[6] != " "

    # if Any Diagonal has a Match, flag that there is Win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the Winner "X" 0r "O"
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    # Set Global Variable
    global game_still_going

    if " " not in board:
        game_still_going = False
    return


def flip_player():
    # Set Global Variable
    global current_player

    # Change Current Player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()

# ------ Operations in Tic Tac Toe Game -----------
# board
# display board
# play game
# handel turn
# check win
    # check row
    # check columns
    # check diagonal
# check tie
# flip player
