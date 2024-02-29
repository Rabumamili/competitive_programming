class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        n = len(nums)
        for i in range(n-2, -1,-1):
            part = ceil(nums[i] / nums[i+1])
            op += part - 1
            rem = nums[i] // part

            if rem == 0:
                nums[i] = nums[i+1]
            else:
                nums[i] = rem
        return op