class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        nums = set(stones)
        @cache
        def dp(i, k):
            if i==stones[-1]:
                return True
            if i not in nums or k == 0:
                return False
            return dp(i+k, k+1) or dp(i+k, k) or dp(i+k, k-1)
        return dp(0,1)


            
             