class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total_sum = sum(stones)
        target = total_sum // 2
        @cache
        def dp(i, current_sum):
            if current_sum == 0:
                return True
            if i == 0:
                return False
            result = dp(i - 1, current_sum)
            if current_sum >= stones[i - 1]:
                result = result or dp(i - 1, current_sum - stones[i - 1]) 
            return result
        for sum_candidate in range(target, -1, -1):
            if dp(n, sum_candidate):
                return total_sum - 2 * sum_candidate
    