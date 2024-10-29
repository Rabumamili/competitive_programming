class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        a = max(nums)
        l = a
        for i in range(1, k):
            l += a+i
        return l