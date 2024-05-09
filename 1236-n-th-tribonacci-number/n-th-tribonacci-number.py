class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dp(n):
            if n < 3:
                return 1 if n else 0
            return dp(n-3) + dp(n-2) + dp(n-1)
        return dp(n)
         