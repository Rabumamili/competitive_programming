
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache
        def dp(i, has_stock):
            if i == len(prices):
                return 0
            
            if has_stock:
                return max(dp(i + 1, has_stock), prices[i] - fee + dp(i + 1, False))
            else:
                return max(dp(i + 1, has_stock), -prices[i] + dp(i + 1, True))
        
        return dp(0, False)
