def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True
print("Ahmed Shaikh 323")

def solve_nqueens(board, col):
    print(f"board : {board}")
    print(f"col : {col}")
    # If all queens are placed
    if col >= len(board):
        return True

    # Try placing a queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            print(f" TRUE is_safe({board}, row{i}, col{col})== true  ")
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_nqueens(board, col + 1):
                print(f" .......... ")
                print(f" .......... ")
                print(f"solve nqueens came true for row :: {i} and col : {col}")
                print(f"solve nqueens came true board :: {board}")
                print(f" .......... ")
                print(f" .......... ")
                return True

            # If placing the queen leads to a solution, return true
            # If not, backtrack: remove the queen and try the next position
            print(f" .......... ")
            print(f" .......... ")
            print(f"Just before Back tracking ... for row :: {i} and col : {col}")
            print(f" Just before Back tracking ... board: {board}")
            board[i][col] = 0
            print(f"Just after Back tracking ... for row :: {i} and col : {col}")
            print(f" Just after Back tracking ... board: {board}")
            print(f" .......... ")
            print(f" .......... ")
        else:
            print(f" FLASE is_safe({board}, row{i}, col{col})== false  ")
    return False

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))

def solve_4queens():
    # Create a 4x4 chess board
    board = [[0, 0, 0, 0] for _ in range(4)]

    if solve_nqueens(board, 0):
        print_board(board)
    else:
        print("No solution exists")

# Run the 4-Queen Problem solver
solve_4queens()
