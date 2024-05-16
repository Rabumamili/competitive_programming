class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*n
        for i in range(n-1, -1, -1):
            solve = questions[i][0] + dp[i+questions[i][1]+1] if i+questions[i][1] + 1 < n else questions[i][0] 
            notsolve = dp[i + 1] if i+1 < n else 0
            dp[i] = max(solve, notsolve)
        return dp[0]