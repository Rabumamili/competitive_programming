class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            return 1
        memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
