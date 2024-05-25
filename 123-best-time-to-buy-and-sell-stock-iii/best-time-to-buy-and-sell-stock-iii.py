class Solution:
    def maxProfit(self, prices: List[int]) -> int:
 
        if not prices:
            return 0
        
        n = len(prices)
        max_left = [0] * n
        min_p = prices[0]
        for i in range(1, n):
            min_p = min(min_p, prices[i])
            max_left[i] = max(max_left[i-1], prices[i] - min_p)
        
        # Second transaction: max profit from each day to the end
        max_right = [0] * n
        max_p = prices[-1]
        for i in range(n-2, -1, -1):
            max_p = max(max_p, prices[i])
            max_right[i] = max(max_right[i+1], max_p - prices[i])
        
        # Combine the results
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_left[i] + max_right[i])
        
        return max_profit