class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        ans = 0
        curr = 0
        
        for num in nums:
            if num == max_value:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 0
    
        ans = max(ans, curr)
        
        return ans