import random


# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


# Function to check if any player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Function to check if the game is a draw
def check_draw(board):
    for row in board:
        if any(cell == 0 for cell in row):
            return False
    return True


# Function to get the user's move
def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9 or board[(move - 1) // 3][(move - 1) % 3] != 0:
                print("Invalid move! Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input! Try again.")


# Function to get the computer's move using a simple AI strategy
def get_computer_move(board):
    # Check if computer can win in the next move
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1
                if check_win(board, -1):
                    return 3 * i + j + 1
                else:
                    board[i][j] = 0

    # Check if player can win in the next move and block them
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1
                if check_win(board, 1):
                    return 3 * i + j + 1
                else:
                    board[i][j] = 0

    # Choose a random available move
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    move = random.choice(available_moves)
    return 3 * move[0] + move[1] + 1


# Main game loop
def play_game():
    board = [[0, 0, 0] for _ in range(3)]
    display_board(board)

    while True:
        # Get user's move
        user_move = get_user_move(board)
        board[(user_move - 1) // 3][(user_move - 1) % 3] = 1
        display_board(board)

        # Check if the user wins
        if check_win(board, 1):
            print("Congratulations! You win!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print("It's a draw!")
            break

        # Get computer's move
        computer_move = get_computer_move(board)
        board[(computer_move - 1) // 3][(computer_move - 1) % 3] = -1
        print("Computer's move:", computer_move)
        display_board(board)

        # Check if the computer wins
        if check_win(board, -1):
            print("Computer wins! Better luck next time.")
            break

        # Check if the game is a draw
        if check_draw(board):
            print("It's a draw!")
            break


# Start the game
play_game()
