class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        oper = 0
        n = len(nums)
        for i in range(n-2, -1,-1):
            partitions = math.ceil(nums[i] / nums[i+1])
            oper += partitions - 1
            remainder = nums[i] // partitions

            if remainder == 0:
                nums[i] = nums[i+1]
            else:
                nums[i] = remainder
        return oper