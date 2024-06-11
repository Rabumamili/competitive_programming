class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = set(nums) 
        maxi = max(nums)
        for i in range(1, max(nums)+1):
            if i not in arr:
                return i
        return maxi+1 if  maxi >= 0 else 1
