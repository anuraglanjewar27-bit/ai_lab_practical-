N = 8

board = [[0]*N for _ in range(N)]


def safe(row, col):

    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1),
                    range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1),
                    range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True


def solve(row):

    if row == N:
        return True

    for col in range(N):

        if safe(row, col):

            board[row][col] = 1

            if solve(row+1):
                return True

            board[row][col] = 0

    return False


if solve(0):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("No Solution")

