class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        n = len(nums)
        i = 0
        while i < n:
            if i > max_reachable:
                return False
            max_reachable = max( max_reachable, i + nums[i])
            if i >= n-1:
                return True
            i += 1
        return False