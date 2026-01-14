import math

def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for i, row in enumerate(board):
        print('|'.join(row))
        if i < 2: print('-' * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ': return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ': return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ': return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ': return board[0][2]
    if all(cell != ' ' for row in board for cell in row): return 'Draw'
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return -1
    elif winner == 'O': return 1
    elif winner == 'Draw': return 0

    best_score = -math.inf if is_maximizing else math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O' if is_maximizing else 'X'
                score = minimax(board, depth + 1, not is_maximizing)
                board[i][j] = ' '
                best_score = max(score, best_score) if is_maximizing else min(score, best_score)
    return best_score

def best_move(board):
    best_score, move = -math.inf, (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score, move = score, (i, j)
    return move

def play_game():
    board = init_board()
    print("You are X, AI is O")
    while True:
        print_board(board)
        try:
            row, col = map(int, input("Enter move (row col): ").split())
            if not (0 <= row < 3 and 0 <= col < 3) or board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
            board[row][col] = 'X'
        except (ValueError, IndexError):
            print("Invalid input. Use format: row col (e.g., 0 1)")
            continue

        if (result := check_winner(board)):
            print_board(board)
            print("Draw!" if result == 'Draw' else f"{result} wins!")
            break

        board[best_move(board)[0]][best_move(board)[1]] = 'O'
        if (result := check_winner(board)):
            print_board(board)
            print("Draw!" if result == 'Draw' else f"{result} wins!")
            break

play_game()
