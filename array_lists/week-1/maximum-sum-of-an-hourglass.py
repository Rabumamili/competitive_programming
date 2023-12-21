class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        hglass = 0

        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                row1  = grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1]
                row2  = grid[row][col]
                row3  = grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
                rows_sum = row1 + row2 + row3
                hglass = max(hglass, rows_sum)

        return hglass