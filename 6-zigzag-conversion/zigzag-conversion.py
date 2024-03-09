class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cur_row = 0
        flag = False

        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                flag = not flag
            cur_row += 1 if flag else -1

        result = ''.join(rows)
        return result