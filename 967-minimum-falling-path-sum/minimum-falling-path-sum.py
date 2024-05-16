class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {} 
        m = len(matrix)
         
        def dp(i, j):
            if i ==0 and j < m:
                return matrix[i][j]
            if j < 0 or j >= m or i < 0:
                return float("inf")
            if (i, j) not in memo:
                memo[(i,j)] = matrix[i][j]+ min([dp(i-1, j-1),dp(i-1, j), dp(i-1, j+1)])
            return memo[(i, j)]
        ans = float('inf')
        for j in range(m):
            ans = min(ans, dp(m-1, j))
        return ans