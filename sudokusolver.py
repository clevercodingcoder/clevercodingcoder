def is_valid_move(board, row, col, num):
    # Check if the number is not present in the row, column, or box
    return (
        num not in board[row] and
        num not in [board[i][col] for i in range(9)] and
        num not in [board[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3) 
                                       for j in range(col // 3 * 3, col // 3 * 3 + 3)]
    )

def find_empty_cell(board):
    # Find an empty cell (represented by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def solve_sudoku(board):
    row, col = find_empty_cell(board)
    if row is None and col is None:
        return True  # All cells filled, the puzzle is solved.

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If the current move leads to a contradiction, backtrack.
            board[row][col] = 0

    return False  # No valid move, need to backtrack.

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells).
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(puzzle):
        print("Sudoku Solved:")
        print_board(puzzle)
    else:
        print("No solution exists for the given Sudoku puzzle.")

# Chatbot made by Clever Coding Coder
# https://www.fiverr.com/wellwithworld?up_rollout=true
# https://github.com/clevercodingcoder/