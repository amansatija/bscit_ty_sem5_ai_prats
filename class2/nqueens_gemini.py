import time

def solve_n_queens(n):
    """
    Solves the N-Queen problem and returns all distinct solutions.

    Args:
        n (int): The size of the chessboard (N x N) and the number of queens.

    Returns:
        list: A list of solutions, where each solution is a list of strings
              representing the board configuration.
    """
    # List to store all valid solutions found.
    solutions = []
    # 'board' will represent the current state of the chessboard.
    # It's a list where board[row] stores the column of the queen in that row.
    # Initialized with -1 indicating no queen placed in any row yet.
    board = [-1] * n

    # Sets to keep track of occupied columns and diagonals for O(1) lookup.
    # 'cols': Stores columns that are already occupied by a queen.
    cols = set()
    # 'pos_diag': Stores sums (row + col) for occupied positive diagonals.
    # Positive diagonals have a constant (row + col).
    pos_diag = set()
    # 'neg_diag': Stores differences (row - col) for occupied negative diagonals.
    # Negative diagonals have a constant (row - col).
    neg_diag = set()

    def backtrack(row):
        """
        Recursive helper function to place queens using backtracking.

        Args:
            row (int): The current row where we are trying to place a queen.
        """
        # Base case: If all N queens are placed (we've successfully placed a queen
        # in 'n' rows), then a solution is found.
        if row == n:
            # Format the current board configuration into a list of strings
            # for display and add it to the solutions list.
            formatted_board = []
            for r in range(n):
                # Create a string for the current row: '.' for empty, 'Q' for queen.
                row_str = ["." for _ in range(n)]
                row_str[board[r]] = "Q" # Place 'Q' at the column where the queen is.
                formatted_board.append("".join(row_str))
            solutions.append(formatted_board)
            return

        # Recursive step: Try placing a queen in each column of the current 'row'.
        for col in range(n):
            # Check if placing a queen at (row, col) is safe.
            # It's safe if the column, positive diagonal, and negative diagonal
            # are all currently unoccupied.
            if col not in cols and \
               (row + col) not in pos_diag and \
               (row - col) not in neg_diag:

                # Place the queen:
                # 1. Mark the column as occupied.
                cols.add(col)
                # 2. Mark the positive diagonal as occupied.
                pos_diag.add(row + col)
                # 3. Mark the negative diagonal as occupied.
                neg_diag.add(row - col)
                # 4. Record the queen's column for the current row in the board array.
                board[row] = col

                # Move to the next row to place the next queen.
                backtrack(row + 1)

                # Backtrack step: If the recursive call returns (meaning no solution
                # was found down that path, or all solutions for that path were found),
                # then "undo" the current queen placement.
                # This allows us to explore other possibilities for the current 'row'.
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row] = -1 # Reset the board position for this row.

    # Start the backtracking process from the first row (row 0).
    backtrack(0)
    return solutions

# --- Main execution part ---
if __name__ == "__main__":
    # Example usage for 4 queens
    n_queens_count = 4
    print(f"Solving {n_queens_count}-Queen problem...")
    start_time = time.time()
    all_solutions = solve_n_queens(n_queens_count)
    end_time = time.time()

    print(f"\nFound {len(all_solutions)} solutions for {n_queens_count} queens:")
    for i, solution in enumerate(all_solutions):
        print(f"--- Solution {i + 1} ---")
        for row_str in solution:
            print(row_str)
        print("-" * (n_queens_count * 2 + 3)) # Separator for readability

    print(f"Time taken: {end_time - start_time:.4f} seconds")

    # You can change n_queens_count to try different board sizes, e.g., 8
    # n_queens_count = 8
    # print(f"\nSolving {n_queens_count}-Queen problem...")
    # start_time = time.time()
    # all_solutions = solve_n_queens(n_queens_count)
    # end_time = time.time()
    # print(f"\nFound {len(all_solutions)} solutions for {n_queens_count} queens.")
    # print(f"Time taken: {end_time - start_time:.4f} seconds")
