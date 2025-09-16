import math

def evaluate(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return 10 if row[0] == "X" else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return 10 if board[0][col] == "X" else -10
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return 10 if board[0][2] == "X" else -10
    return 0

def is_moves_left(board):
    return any(" " in row for row in board)

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score != 0: return score
    if not is_moves_left(board): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

# Example empty board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("Evaluation:", minimax(board, 0, True))
