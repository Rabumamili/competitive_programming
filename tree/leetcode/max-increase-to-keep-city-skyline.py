class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        
        max_increase = 0
        
        for r in range(n):
            for c in range(n):
                max_allowed_height = min(row_max[r], col_max[c])
                max_increase += max_allowed_height - grid[r][c]
        
        return max_increase