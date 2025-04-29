import math

# Initialize the board as a 3x3 list
def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Display the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for a win or draw
def check_winner(board):
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Check for draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = init_board()
    print("You are X, AI is O")
    while True:
        print_board(board)
        user_move = tuple(map(int, input("Enter your move (row col): ").split()))
        if board[user_move[0]][user_move[1]] == ' ':
            board[user_move[0]][user_move[1]] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        result = check_winner(board)
        if result:
            print_board(board)
            if result == 'Draw':
                print("Draw!")
            else:
                print(f"{result} wins!")
            break

        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = 'O'

        result = check_winner(board)
        if result:
            print_board(board)
            if result == 'Draw':
                print("Draw!")
            else:
                print(f"{result} wins!")
            break

play_game()
