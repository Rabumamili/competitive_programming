class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        def dp(i, j):
            if i ==(n-1) and j < len(triangle[i]):
                return triangle[i][j]
            if i >= n or j < 0 or j >= len(triangle[i]):
                return float("inf")
            if (i, j) not in memo:
                memo[(i, j)] = triangle[i][j]+ min(dp(i+1, j+1),dp(i+1, j))
            return memo[(i, j)]
        return dp(0, 0)