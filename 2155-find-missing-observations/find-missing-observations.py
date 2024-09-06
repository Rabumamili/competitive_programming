class Solution:
    def missingRolls(self, r: List[int], mean: int, n: int) -> List[int]:
        m = len(r)
        total_sum = mean * (n + m)
        known_sum = sum(r)
        miss_sum = total_sum - known_sum
        if miss_sum < n or miss_sum > 6 * n:
            return []
        res = [1] * n
        miss_sum -= n  
  
        for i in range(n):
            add_val = min(miss_sum, 5)
            res[i] += add_val
            miss_sum -= add_val
        
        return res