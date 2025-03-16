import copy
import random

def print_board(board):
    print("-" * 17)
    for row in board:
        print("|", " ".join(row), "|")
    print("-" * 17)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_next_open_row(board, col):
    for r in reversed(range(6)):
        if board[r][col] == ' ':
            return r
    return None

def check_win(board, piece):
    for r in range(6):
        for c in range(7):
            if c <= 3 and all(board[r][c+i] == piece for i in range(4)):
                return True
            if r <= 2 and all(board[r+i][c] == piece for i in range(4)):
                return True
            if r <= 2 and c <= 3 and all(board[r+i][c+i] == piece for i in range(4)):
                return True
            if r <= 2 and c >= 3 and all(board[r+i][c-i] == piece for i in range(4)):
                return True
    return False

def minimax(board, depth, alpha, beta, maximizing):
    valid_cols = [c for c in range(7) if board[0][c] == ' ']
    if check_win(board, 'O'):
        return (None, 100)
    if check_win(board, 'X'):
        return (None, -100)
    if depth == 0 or not valid_cols:
        return (None, 0)
    if maximizing:
        value = -float('inf')
        column = random.choice(valid_cols)
        for col in valid_cols:
            row = get_next_open_row(board, col)
            temp = copy.deepcopy(board)
            drop_piece(temp, row, col, 'O')
            new_score = minimax(temp, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return (column, value)
    else:
        value = float('inf')
        column = random.choice(valid_cols)
        for col in valid_cols:
            row = get_next_open_row(board, col)
            temp = copy.deepcopy(board)
            drop_piece(temp, row, col, 'X')
            new_score = minimax(temp, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return (column, value)

def ai_move(board):
    col, _ = minimax(board, 4, -float('inf'), float('inf'), True)
    return col

board = [[' ' for _ in range(7)] for _ in range(6)]
game_over = False
turn = random.randint(0, 1)

while not game_over:
    print_board(board)
    if turn == 0:
        col = int(input("Ваш ход (0-6): "))
        if board[0][col] != ' ':
            continue
    else:
        col = ai_move(board)
    row = get_next_open_row(board, col)
    if row is None:
        continue
    drop_piece(board, row, col, 'X' if turn == 0 else 'O')
    if check_win(board, 'X' if turn == 0 else 'O'):
        print_board(board)
        print("Вы выиграли!" if turn == 0 else "ИИ выиграл!")
        game_over = True
    turn = 1 - turn
    if all(board[0][c] != ' ' for c in range(7)):
        print_board(board)
        print("Ничья!")
        game_over = True
