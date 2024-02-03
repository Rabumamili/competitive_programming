class Solution:
    def maxScore(self, s: str) -> int:
        maxsum= 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count("0")+ right.count('1')
            maxsum = max(maxsum, score)
        return maxsum
