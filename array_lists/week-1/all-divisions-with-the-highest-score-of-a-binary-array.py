class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones= sum(nums)
        left = 0
        right = ones
        ans =[0]
        for i,el in enumerate(nums):
            if el == 0:
                left += 1
            else:
                right -= 1

            if right + left > ones:
                ans = [i+1]
                ones = right + left
            elif right + left == ones:
                ans += [i+1]
        return ans

        