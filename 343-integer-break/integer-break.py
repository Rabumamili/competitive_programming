class Solution:
    def integerBreak(self, n: int) -> int:

        if n == 2 or n == 3:
            return n-1
        
        ans = 1
        while n > 4:
            n -= 3
            ans *=3                
        return ans*n