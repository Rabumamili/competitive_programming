class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            palindrome[i][i] = True
        for i in range(n - 1):
            palindrome[i][i + 1] = (s[i] == s[i + 1])
        
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                palindrome[i][j] = (s[i] == s[j] and palindrome[i + 1][j - 1])
        
        dp = [0] * n
        for i in range(n):
            if palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(i):
                    if palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1] 