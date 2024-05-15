class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}
        def dp(i, j):
            if i == 0 and j == 0 and grid[i][j]!=1:
                return 1
            if i < 0 or j < 0 or grid[i][j]==1:
                return 0
            if (i, j) not in memo:
                memo[(i,j)] = dp(i-1, j)+ dp(i, j-1)
            return memo[(i, j)]

        return dp(m-1, n-1)