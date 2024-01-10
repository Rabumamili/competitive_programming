class Solution(object):
    def maximumUniqueSubarray(self, nums):
        n = len(nums)
        unique_set = set()
        max_score = curscore = 0
        left = 0

        for right in range(n):
            while nums[right] in unique_set:
                unique_set.remove(nums[left])
                curscore -= nums[left]
                left += 1

            unique_set.add(nums[right])
            curscore += nums[right]
            max_score = max(max_score, curscore)

        return max_score