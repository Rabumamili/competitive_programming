class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numSet:
                currentNum = num
                currentL = 1
                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentL += 1
                longest = max(currentL, longest)
        return longest
