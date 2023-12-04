class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * (l * 2)
        ans[:l] = nums
        ans[l:] = nums
        return ans
            