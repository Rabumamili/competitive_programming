class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =1
        high = max(piles)
        k = high

        while low <= high:
            mid = (low + high)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1

        return k
 