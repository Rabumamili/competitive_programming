class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
    
        start = 0
        end = 0
        max_length = 0
        zero_count = 0

        while end < len(nums):
            if nums[end] == 0:
                zero_count += 1

            while zero_count == 2:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            length = end - start 
            max_length = max(max_length, length)

            end += 1

        return max_length