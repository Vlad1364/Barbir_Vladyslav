from random import randrange
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

def print_board(board):
    for row in range(3):
        print("+" + "---+" * 3)
        print("|", end=" ")
        for col in range(3):
            cell_value = board[row][col]
            if cell_value == 'O':
                print(BLUE + cell_value + RESET, end=" | ")
            elif cell_value == 'X':
                print(RED + cell_value + RESET, end=" | ")
            else:
                print(cell_value, end=" | ")
        print()
    print("+" + "---+" * 3)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' and not cell.isdigit() for cell in row) for row in board)

def get_free_positions(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col].isdigit()]

def make_computer_move(board):
    free_positions = get_free_positions(board)
    if free_positions:
        row, col = free_positions[randrange(len(free_positions))]
        board[row][col] = 'X'

def make_user_move(board):
    while True:
        try:
            move = int(input("Enter the number of the square where you want to place 'O' (1-9): "))
            if 1 <= move <= 9:
                row, col = divmod(move - 1, 3)
                if board[row][col].isdigit():
                    board[row][col] = 'O'
                    break
                else:
                    print("This square is already taken. Try again.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print_board(board)

    make_computer_move(board)
    print_board(board)

    while True:
        make_user_move(board)
        print_board(board)

        if check_winner(board, 'O'):
            print(BLUE + "You win!" + RESET)
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        make_computer_move(board)
        print_board(board)

        if check_winner(board, 'X'):
            print(RED + "Computer wins!" + RESET)
            break

        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()