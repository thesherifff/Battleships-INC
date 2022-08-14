# Import function to create integers
from random import randint

board = []
cpu_board = []

for x in range(9):
    """
    Generates area of the play area
    """
    board.append(["-"] * 9)
    cpu_board.append(["_"] * 9)


def c_board(cpu_board):
    """
    Create a layout for CPU's board
    """
    for row in cpu_board:
        print(" ".join(row))


def p_board(board):
    """
    Create a layout for the player's board
    """
    for row in board:
        print(" ".join(row))


def print_boards():
    """
    Print both sets of boards
    """
    print("Your Board:")
    p_board(board)
    print(" ")
    print("CPU's Board:")
    c_board(cpu_board)


def location_col(board):
    """
    Generate a column at random for the computer's ship
    """
    return randint(0, len(board) - 1)


def location_row(board):
    """
    Generate a row at random for the computer's ship
    """
    return randint(0, len(board) - 1)


def cpu_location_col(cpu_board):
    """
    Generate a row at random for the player's
    """
    return randint(0, len(cpu_board) - 1)


def cpu_location_row(cpu_board):
    """
    Generate a column at random for the player's
    """
    return randint(0, len(cpu_board) - 1)


# Logic for the user ships to not generate the same column/row
ship_col = location_col(board)
ship_row = location_row(board)
while True:
    ship_col2 = location_col(board)
    ship_row2 = location_row(board)
    if ship_row2 != ship_row and ship_col2 != ship_col:
        ship_col3 = location_col(board)
        ship_row3 = location_row(board)
        if (ship_row3 != ship_row2 and ship_col3 != ship_col2) and \
                (ship_row3 != ship_row and ship_col3 != ship_col):
            break


# Logic for the CPU to not generate the same guesses
cpu_ship_col = cpu_location_col(cpu_board)
cpu_ship_row = cpu_location_row(cpu_board)
while True:
    cpu_ship_col2 = location_col(board)
    cpu_ship_row2 = location_row(board)
    if cpu_ship_row2 != cpu_ship_row and cpu_ship_col2 != cpu_ship_col:
        cpu_ship_col3 = location_col(board)
        cpu_ship_row3 = location_row(board)
        if (cpu_ship_row3 != cpu_ship_row2 and
            cpu_ship_col3 != cpu_ship_col2) and \
            (cpu_ship_row3 != cpu_ship_row and
                cpu_ship_col3 != cpu_ship_col):
            break


def print_cpu_guess():
    """
    Print CPU guess row and col function
    """
    print("The CPU guessed:")
    print(f"Column: {cpu_guess_col + 1}, Row: {cpu_guess_row + 1}")


def welcome_instructions():
    """
    Intructions explaioning how the game is played.
    """
    print("Welcome to the famous game known as Battleship!")
    print("A Column is defined as going from left to right")
    print("A Row is defined as going from up to down")
    print("Board size: 9x9. Upper left corner is col: 1, row: 1")
    print("Number of ships: 3 for each player")
    print("You have 8 tries before the game forfeits!")
    print("To play again, please select run program")


# logic
hit_count = 0
cpu_hit_count = 0
welcome_instructions()
# Display user ships on their board
board[ship_col][ship_row] = "S"
board[ship_col2][ship_row2] = "S"
board[ship_col3][ship_row3] = "S"
print_boards()
guess = 0
cpu_guess_col_row_validation = []
while guess < 9:
    # After 8 turns the game will end.
    if guess == 8:
        print("Sorry, You loose! Too many incorrect guesses.")
        break

    print("Turn: " + str(guess + 1))

    # Validation to check that user input is an integer
    while True:
        try:
            guess_col = int(input("Guess Column: ")) - 1
            guess_row = int(input("Guess Row: ")) - 1
            break
        except ValueError:
            print("Not an integer. Try Again")
            continue

# Generates CPU guess, if its has been generated then try new colum/row
    while True:
        cpu_guess_col = randint(0, len(board) - 1)
        cpu_guess_row = randint(0, len(board) - 1)

        if [cpu_guess_row, cpu_guess_col] in cpu_guess_col_row_validation:
            continue
        else:
            cpu_guess_col_row_validation.append([cpu_guess_row, cpu_guess_col])
            break

    # Logic for if user is correct
    if (guess_row == cpu_ship_row and
        guess_col == cpu_ship_col) \
        or (guess_row == cpu_ship_row2 and guess_col == cpu_ship_col2) \
            or (guess_row == cpu_ship_row3 and guess_col == cpu_ship_col3):
        cpu_board[guess_row][guess_col] = "X"
        hit_count = hit_count + 1
        if hit_count == 1:
            print("You sank the first CPU battleship!")
        elif hit_count == 2:
            print("You sank the second CPU battleship!")
        elif hit_count == 3:
            print("Well done! You sunk all of the CPU's battleships!")
            print("Game over! You win!")
            print_boards()
            break
        # Logic for if CPU is correct
        if (cpu_guess_row == ship_row and cpu_guess_col == ship_col) or \
            (cpu_guess_row == ship_row2 and cpu_guess_col == ship_col2) or \
                (cpu_guess_row == ship_row3 and cpu_guess_col == ship_col3):
            board[cpu_guess_row][cpu_guess_col] = "X"
            print_boards()
            print_cpu_guess()
            cpu_hit_count = cpu_hit_count + 1
            if cpu_hit_count == 1:
                print("The CPU sank your first ship!")
            elif cpu_hit_count == 2:
                print("The CPU sank your second ship!")
            elif cpu_hit_count == 3:
                print("Well that is Game over! The CPU sank all 3 ships!")
                print("Game over! You lost! Please try again!")
                print_boards()
                break
        else:
            # Logic for if CPU is incorrect
            board[cpu_guess_row][cpu_guess_col] = "O"
            print_boards()
            print_cpu_guess()
            print("The CPU has missed!")
        guess += 1
    else:
        # Logic for if user chooses a value that is not in range
        if guess_row not in range(7) or guess_col not in range(7):
            print("Oh no!, the value is not in range")
            print_boards()
        # Logic for if user guesses selects a previously selected guess.
        elif cpu_board[guess_row][guess_col] == "X" or \
                cpu_board[guess_row][guess_col] == "O":
            print("You have already guessed here")
            print_boards()
        else:
            # Logic for if user guesses incorrectly
            cpu_board[guess_row][guess_col] = "O"
            print("Unlucky, you missed. Try again!")
            # Logic for if CPU guesses correctly
            if (cpu_guess_row == ship_row and
                cpu_guess_col == ship_col) or \
                (cpu_guess_row == ship_row2 and
                    cpu_guess_col == ship_col2) or \
                (cpu_guess_row == ship_row3 and
                    cpu_guess_col == ship_col3):
                board[cpu_guess_row][cpu_guess_col] = "X"
                print_boards()
                print_cpu_guess()
                cpu_hit_count = cpu_hit_count + 1
                if cpu_hit_count == 1:
                    print("The CPU sank your first battleship!")
                    guess = + 1
                elif cpu_hit_count == 2:
                    print("The CPU sank your second battleship!")
                    guess = + 1
                elif cpu_hit_count == 3:
                    print("The CPU sunk all your battleships!")
                    guess = + 1
                    print("Game over! You lost!")
                    print_boards()
                    break
            else:
                # Logic for if CPU guesses incorrectly
                board[cpu_guess_row][cpu_guess_col] = "O"
                print_boards()
                print_cpu_guess()
                print("The CPU missed!")
            guess += 1

print("To run the game again, select run program")
