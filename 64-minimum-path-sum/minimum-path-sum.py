class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}
        
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float("inf")
            if (i, j) not in memo:
                memo[(i, j)] = min(grid[i][j]+dp(i-1,j),grid[i][j]+ dp(i, j-1) )
            return memo[(i, j)]
        return dp(m-1, n-1)

 