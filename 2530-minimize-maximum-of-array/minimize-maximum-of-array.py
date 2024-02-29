class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        cumSum = 0
        for idx,num in enumerate(nums):
            cumSum += num
            ans = max(ans, ceil(cumSum/(idx+1)))
        return ans