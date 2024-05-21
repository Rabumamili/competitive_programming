class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            count = dp(i+1, j)
            if s[i] == t[j]:
                count += dp(i+1, j+1)
           
            return count
        return  dp(0, 0)