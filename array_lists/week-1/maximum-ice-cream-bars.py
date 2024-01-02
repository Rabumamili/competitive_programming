class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_price = max(costs) + 1
        count = [0] * max_price

        for cost in costs:
            count[cost] += 1

        total_bars = 0

        for price in range(max_price):
            while coins >= price and count[price] > 0:
                coins -= price
                total_bars += 1
                count[price] -= 1

        return total_bars