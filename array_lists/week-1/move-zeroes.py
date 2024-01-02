class Solution(object):
    def moveZeroes(self, nums):
        left= 0
        for right in range(len(nums) ):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
        # zero = 0
        # zero = nums.count(0)
        # return [nums[i] for i in range(len(nums)) if nums[i]!=0] +([0]*zero)