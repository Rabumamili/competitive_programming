class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit != '.':
                    if digit in rows[i] or digit in columns[j] or digit in sub_boxes[(i // 3) * 3 + (j // 3)]:
                        return False
                    rows[i].add(digit)
                    columns[j].add(digit)
                    sub_boxes[(i // 3) * 3 + (j //3)].add(digit)

        return True