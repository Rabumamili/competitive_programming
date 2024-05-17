class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]
        @cache
        
        def dp(r, c, m):
            
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
             
            if m == 0:
                return 1
            
            prob = 0
            for dr, dc in moves:
                prob += dp(r + dr, c + dc, m - 1) / 8.0
             
            return prob
        
        return dp(row, column, k)
