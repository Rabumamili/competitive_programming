class Solution:
    def maxScore(self, s: str) -> int:
        maxsum = 0
        for i in range(len(s)-1):
            sums = s[:i+1].count("0") + s[i+1:].count("1")
            maxsum = max(sums, maxsum)
        return maxsum
     