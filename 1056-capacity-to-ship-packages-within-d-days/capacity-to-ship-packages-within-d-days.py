class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            capacity = (low + high) // 2
            cur_weight = 0
            time = 1
            for weight in weights:
                cur_weight += weight
                if cur_weight > capacity:
                    time += 1
                    cur_weight = weight
            if time > days:
                low = capacity + 1
            else:
                high = capacity
        return low
