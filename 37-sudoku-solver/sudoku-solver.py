class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
   
        def is_valid(row, col, num):
            # Check if the number is already present in the row or column
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False

            # Check if the number is present in the 3x3 sub-grid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True

        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = "."  # Backtrack if the solution is not valid
                        return False
            return True

        solve()
    