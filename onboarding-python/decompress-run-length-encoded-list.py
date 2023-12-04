class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        num = []
        for i in range(0, len(nums), 2):
            num += [nums[i+1]] * nums[i]
        return num