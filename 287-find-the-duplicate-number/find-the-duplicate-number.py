class Solution(object):
    def findDuplicate(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            idx = nums[i]-1
            if idx != i:
                if nums[idx]!= nums[i]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                else:
                    i += 1
            else:
                i += 1
        for i in range(n):
            if nums[i] != i +1:
                return nums[i]
 