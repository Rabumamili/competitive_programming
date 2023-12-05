class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxperimeter = 0
        for i in range(2, len(nums)):
            if nums[i]< nums[i-1]+nums[i-2]:
                perimeter =nums[i]+nums[i-1]+nums[i-2]
                maxperimeter = max(perimeter, maxperimeter)
        return maxperimeter
