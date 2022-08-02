import random
# A Import random  to be able to create integers(random)


def build_board(dims):
    return[['O' for count in range(dims)]for count in range(dims)]

# Create a square board that is pulled from "dims" value
build_board(8)

[['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O']]


def print_board(board):
    for b in board:
        print(*b)

board = build_board(8)
print_board(board)


# Return ship positional coordinates.
def build_ship(dims):
    # Length of ship is length of board and random number between 2.
    len_ship = random.randint(2, dims)
    orientation = random.randint(0, 1)
    # Ship is vertical if orientation is 1 and horizontal if orientation is 0
    if orientation == 0:
        # Select at random a row and create a list of selected row * ships length
        row_ship = [random.randint(0, dims - 1)] * len_ship
        # Select a column at random of the ships first position (why we subtract ships length)
        col = random.randint(0, dims - len_ship)
        # List of created colum values
        col_ship = list(range(col, col + len_ship))
        # Positional values from row and column lists that have been created.
        coords = tuple(zip(row_ship, col_ship))
    else:
        # Switched positional values of§ column and row
        col_ship = [random.randint(0, dims - 1)] * len_ship
        row = random.randint(0, dims - len_ship)
        row_ship = list(range(row, row + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)

ship = build_ship(4); ship

# Ship data
[(1, 1), (2, 1), (3, 1)]


def user_guess():
    row = int(input('Row: ')) - 1
    col = int(input('Col: ')) - 1
    return (row, col)

x = user_guess(); x

Row: 1
Col: 1


(0, 0)


def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print('Really? I already told you there was nothing there!')
        return board
    guesses.append(guess)
    if guess in ship:
        print('Downed but not out!')
        # Notify players with 'X' confirming hit.
        board[guess[0]][guess[1]] = 'X'
        # Remove above value from ship coordinates; helpful to use for while loop in main()
        ship.remove(guess)
        return board
    print('Go again!')
    return board

# List of guesses
guesses = []
our_guess = user_guess()
board = update_board(our_guess, board, ship, guesses)
print_board(board)


def welcome_message():
    print('Battleship Awaits!')
    print('There are battleships lurking around, hidden in the board. Enter a row and coloum guesses to destroy the ships!')<
welcome_message()


def main():
    welcome_message()
    board = build_board(5)
    ship = build_ship(5)
    guesses = []
    while len(ship) > 0:
        board = update_board(user_guess(), board, ship, guesses)
        print_board(board)
    print('You sunk my battleship!')
    return

main()
