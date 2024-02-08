class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub =float ("-inf")
        sumsub = 0
        if len(nums) ==1:
            return nums[0]
        for num in nums:
            sumsub += num
            maxsub = max(sumsub, maxsub)
            if sumsub < 0:
                sumsub = 0
        return maxsub