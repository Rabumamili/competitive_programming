class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums = sorted(heights)
        ans = 0
        for i in range(len(nums)):
            if nums[i]!=heights[i]:
                ans += 1
        return ans