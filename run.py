

user = []
user_guesses = []
comp = []


from random import randint

user = []
user_guesses = []
comp = []


def make_board(board):
    """
    Make the starting board of 5 "X" in 5 lists
    Arguments: an empty list
    Returns: a list containing 5 lists of the letter X
    """
    for i in range(5):
        board.append([" X "]*5)
    return board


def print_board(board):
    """
    Prints the board lists of X, removing list formatting and
    adding spaces
    Argument: a list
    """
    for ind in board:
        print(" ".join(ind))


def random_num(board):
    """
    Generate a random number between 0 and the length of the board minus one.
    We minus 1 because len starts at 1 but the board's lists start at 0
    Argument: a list (expected to be the player's board)
    """
    return randint(0, len(board)-1)


def generate_ship_loc(board):
    """
    We want 4 ships to be on the board and the while loop ensures there will
    be. It generates random co-ordinates, places the "o", then counts how many
    "o" are in the board's lists, keeping track with variable ship_num. If that
    number is less than 4, it loops again. This should catch if any locations
    are randomly generated more than once.
    Argument: a list, expected to be the populated players board
    """
    ship_num = 0
    while ship_num < 4:  # we want 4 ships to be on the board
        ship_num = 0  # reset ship_num value every loop
        ship_col = random_num(board)
        ship_row = random_num(board)
        board[ship_row][ship_col] = " o "
        # for every list in the board, we look for " o " and keep a running
        # total with ship_num
        for row in board:
            ship_num += row.count(" o ")


def welcome():
    """
    Opening message to the game that also takes in a username.
    """
    print("Welcome to you vs. computer Battleships!")
    username = input("Type in a username and press return: \n")
    print(f'\nHi {username}! We will auto generate your battleship locations.'
          'You have 4 battleships to find within the computer\'s board.')
    print('\nX are empty locations, * are shots that missed and # are hits'
          'Be aware that the grid is five wide using integers between 1 and 5')


def generate_boards():
    """
    Creates all the boards ready for use. A user board which will house the
    user's battleships that the computer will try to find. The comp board is
    the computer board housing the computer's battleships but the user_guesses
    board will be the version of the computer board shown to the user - we
    don't want to show the user where the computer's ships are!
    """
    make_board(user)
    make_board(comp)
    make_board(user_guesses)
    generate_ship_loc(user)
    generate_ship_loc(comp)


def user_guess():
    """
    Get user input on battleship guess, check whether it is valid data,
    check whether that shot has already been taken, check whether they hit a
    battleship and show them the result of their turn.
    """
    print("Here is the computer's board:")
    print_board(user_guesses)
    repeat = True
    while repeat:
        # check whether data is valid
        while True:
            print("\nWhich column would you like to fire at?")
            guess_col = input("Enter a number and press enter: \n")
            if validate_data(guess_col):
                break
        while True:
            print("\nWhich row would you like to fire at?")
            guess_row = input("Enter a number and press enter: \n")
            if validate_data(guess_row):
                break

        # minus 1 as the users enter numbers between 1 and 5
        guess_col = int(guess_col)-1
        guess_row = int(guess_row)-1

        # check if we've already chosen that spot
        if (user_guesses[guess_row][guess_col] == " * " or
                user_guesses[guess_row][guess_col] == " # "):
            print("You've already picked that spot, try again!")
        else:
            repeat = False
    # Check whether that spot is a hit or not and display result
    if comp[guess_row][guess_col] == " o ":
        user_guesses[guess_row][guess_col] = " # "
        print("\nYAY! You hit their ship!")
    else:
        user_guesses[guess_row][guess_col] = " * "
        print("\nOh no! You missed their ship :(")


def comp_guess():
    """
    Computer guess at user board using randomly generate co-ordinates
    """
    print("\n\nNow the computer's turn!")
    repeat = True
    # Generate first random numbers
    guess_col = random_num(comp)
    guess_row = random_num(comp)
    # Check if we've already chosen that spot
    while repeat:
        if (user[guess_row][guess_col] == " * " or
                user[guess_row][guess_col] == " # "):
            guess_col = random_num(comp)
            guess_row = random_num(comp)
        else:
            repeat = False
    # Display to the user what the computer chose and result
    print(f"They've chosen {guess_col + 1}, {guess_row + 1}")
    if user[guess_row][guess_col] == " o ":
        user[guess_row][guess_col] = " # "
        print("It's a hit! :(")
    else:
        user[guess_row][guess_col] = " * "
        print("YAY! They missed!")


def game_play():
    """
    Main loop for playing the game. First generate the boards and display the
    welcome message. Then, there's a while loop so that we can take a maximum
    of then turns. In the while loop, we display with turn it is, then run the
    user guess, print and computer guess functions. Then each turn, we check
    whether there is a winner, if there is, we exit the loop and run the final
    winning check and message function. If after all the turns, there is no
    winner, we still run the final winning check function.
    """
    generate_boards()
    welcome()
    i = 0
    while i < 10:
        print(f"\nThis is turn {i +1}/10 \n")
        user_guess()
        print_board(user_guesses)
        input("\nPress Enter to continue...")
        comp_guess()
        print("\nHere's your board: ")
        print_board(user)
        input("\nPress Enter to continue...")
        i += 1
        if check_winner(user) == 4:
            i = 10
        elif check_winner(user_guesses) == 4:
            i = 10
    check_winner_final()


def validate_data(value):
    """
    If values is not between 1 and 5, raise an error and request a new input
    Argument: user input value
    """
    try:
        if int(value) > 5 or int(value) < 1:
            raise ValueError(
                "Your shot is out of bounds! Choose a number between 1 and 5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        print("Please enter an integer between 1 and 5")
        return False
    return True


def check_winner(board):
    """
    Sums the number of times " # " (hit battleships) appear in the board.
    Argument: a list, expected to be the player board
    """
    total = 0
    for list in board:
        total += list.count(" # ")
    return total


def check_winner_final():
    """
    Check for a winner after ten turns and report the result to the user
    """
    user_result = check_winner(user_guesses)
    comp_result = check_winner(user)
    if user_result > comp_result:
        print("Congratulations! You WIN!")
    elif user_result < comp_result:
        print("Commiserations - the computer had the most hits!")
    else:
        print("It was a draw!")


# Call the main function
game_play()
