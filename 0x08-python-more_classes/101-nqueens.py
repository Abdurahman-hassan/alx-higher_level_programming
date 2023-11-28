#!/usr/bin/python3
"""N queens puzzle"""


def isSafe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, n, result):
    """Solve N Queen problem"""

    # base case: If all queens are placed
    # then return true
    if col == n:
        temp = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    temp.append([i, j])
        result.append(temp)
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    res = False
    for i in range(n):

        # Check if queen can be placed on
        # board[i][col]
        if isSafe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Make result true if any placement
            # is possible
            res = solveNQUtil(board, col + 1, n, result) or res

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if queen can not be place in any row in
    # this colum col then return false
    return res


def solveNQ(n):
    """Solve N Queen problem"""

    board = [[0 for j in range(n)] for i in range(n)]
    result = []
    solveNQUtil(board, 0, n, result)
    return result


def printBoard(board):
    """Print the board"""

    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    result = solveNQ(n)
    for i in result:
        print(i)
