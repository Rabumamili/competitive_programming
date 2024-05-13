class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = {}
        def dp(i, j):
            if i >= n or j >= m:
                return 0
            if (i, j) not in memo:
                if text1[i] == text2[j]:
                    memo[(i, j)] = 1 + dp(i+1, j+1)
                else:
                    memo[(i, j)] = max(dp(i+1, j), dp(i, j+1))
            return memo[(i,j)]

        return dp(0, 0)
            


    