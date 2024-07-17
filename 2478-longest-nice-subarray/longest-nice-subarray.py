class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 0
        current = 0
        start = 0

        for end in range(len(nums)):
             
            while (current& nums[end]) != 0:
                current ^= nums[start]
                start += 1
       
            current|= nums[end]
            max_len = max(max_len, end - start + 1)
        
        return max_len