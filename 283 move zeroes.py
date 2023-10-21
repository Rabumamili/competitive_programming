class Solution(object):
    def moveZeroes(self, nums):
        zero_count = nums.count(0)
        next_non_zero = 0
        for n in nums:
            if n != 0:
                nums[next_non_zero] = n
                next_non_zero += 1

        for zero in range(1, zero_count + 1):
            nums[-zero] = 0
