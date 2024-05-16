class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        n = len(piles)
        
        def dp(i, j):
            if i == j:
                return piles[i]
            if (i, j) not  in memo:
                memo[(i, j)] = max(piles[i] - dp(i+1, j), piles[j] - dp(i, j-1))
            return memo[(i, j)]
        
        return dp(0, n-1) > 0
        
             
