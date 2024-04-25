class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()

        if len(nums) % 2 == 0:
            median = (len(nums) + 2) // 2 - 1
        else:
            median = (len(nums) + 1) // 2 - 1
        
        op = abs(k - nums[median])
        if k < nums[median]:
            for index in range(median):
                if nums[index] > k:
                    op += nums[index] - k
        elif k > nums[median]:
            for index in range(median + 1 , len(nums)):
                if nums[index] < k:
                    op += k - nums[index]
        return op