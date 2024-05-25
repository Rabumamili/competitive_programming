class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
    
        n = len(prices)
        if k >= n // 2:
            
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit
        
        dp_buy = [-float('inf')] * (k + 1)
        dp_sell = [0] * (k + 1)
        
        for price in prices:
            for j in range(1, k + 1):
                dp_buy[j] = max(dp_buy[j], dp_sell[j - 1] - price)
                dp_sell[j] = max(dp_sell[j], dp_buy[j] + price)
        
        return dp_sell[k]