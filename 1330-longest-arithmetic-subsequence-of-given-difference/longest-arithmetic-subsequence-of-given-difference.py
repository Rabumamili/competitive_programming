class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        maxi = 0
        
        for x in arr:
            prev = x - difference
            if prev in dp:
                dp[x] = dp[prev] + 1
            else:
                dp[x] = 1
            maxi = max(maxi, dp[x])
        
        return maxi