class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total= sum(nums)
        prev = 0

        for i, num in enumerate(nums):
            total -= num

            if prev == total:
                return i

            prev += num

        return -1