class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, n):
            if i >= len(coins) or n <=0:
                if n==0:
                    return 1
                else:return 0
            if (i, n) not in memo:
                memo[(i,n)] = dp(i, n-coins[i]) + dp(i+1, n)
            return memo[(i, n)]
        return dp(0, amount)