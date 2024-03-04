class Solution:
    def totalNQueens(self, n: int) -> int:
         
        def is_not_under_attack(row, col):
            for prev_row in range(row):
                if board[prev_row] == col or board[prev_row] - prev_row == col - row or board[prev_row] + prev_row == col + row:
                    return False
            return True

        def place_queen(row):
            if row == n:
                # Found a solution
                solutions.append(list(board))
                return
            for col in range(n):
                if is_not_under_attack(row, col):
                    board[row] = col
                    place_queen(row + 1)

        board = [-1] * n
        solutions = []
        place_queen(0)

        return len(solutions)

 