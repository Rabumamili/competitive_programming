class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            
            if n == 2 or n == 3:
                return n-1
            
            ans = 1
            while n > 4:
                n -= 3
                ans *=3                
            memo[n] = ans*n
            return memo[n]
        
        return dp(n)