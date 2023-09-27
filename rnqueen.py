
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col == 8:
        print_board(board)
        return True

    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens(board, col + 1)
            board[i][col] = 0

    return False

def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()
    print()

board = [[0 for x in range(8)] for y in range(8)]

solve_n_queens(board, 0)
