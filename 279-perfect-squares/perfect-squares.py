class Solution:
    def numSquares(self, n: int) -> int:
 
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  
        k = int(n**0.5)+1
        squares = [i * i for i in range(1, k)]
        
         
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]

    