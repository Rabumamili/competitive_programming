class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return right