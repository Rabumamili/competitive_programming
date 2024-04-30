class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = nums[0]
        for i in range(1,len(nums)):
            result ^= nums[i]
        return bin(k^result).count("1")