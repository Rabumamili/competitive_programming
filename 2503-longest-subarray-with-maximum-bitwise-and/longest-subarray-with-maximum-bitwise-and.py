class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        longest_length = 0
        current_length = 0
        
        for num in nums:
            if num == max_value:
                current_length += 1
            else:
                longest_length = max(longest_length, current_length)
                current_length = 0
    
        longest_length = max(longest_length, current_length)
        
        return longest_length