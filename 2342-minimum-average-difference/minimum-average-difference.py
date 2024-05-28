class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sum_nums, n, min_avg_diff = sum(nums), len(nums), (float('inf'), -1)
        left_sum = 0
        for i in range(n):
            left_sum += nums[i]
            left_avg = left_sum // (i + 1)
            
            right_sum = sum_nums - left_sum
            right_avg = (right_sum // (n - i - 1)) if right_sum > 0 else 0

            avg_diff = abs(left_avg - right_avg)
            if avg_diff < min_avg_diff[0]:
                min_avg_diff = (avg_diff, i)
        
        return min_avg_diff[1]