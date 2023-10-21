class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        sum = 0
        l, r = 0, len(piles) - 2
        while l < r:
            sum += piles[r]
            l += 1
            r -= 2
        return sum
