class Solution:
    def maxPossibleScore(self, nums: List[int], d: int) -> int:
        n = len(nums)
        nums.sort()

        def solve(diff):
            prev = nums[0]
            for i in range(1, n):
                curr = prev+diff
                if curr>nums[i]+d:
                    return False
                elif curr<nums[i]:
                    prev = nums[i]
                else:
                    prev = curr
            return True


        res = 0
        l = 0
        r = nums[-1]-nums[0]+d
        while l<=r:
            m = (l+r)//2
            if solve(m):
                res = m
                l=m+1
            else:
                r=m-1
        
        return res