class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        char = set(s)
        for i in range(len(s)):
            if not (s[i].lower() in char and s[i].upper() in char):
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                if len(right) > len(left):
                    return right
                else:
                    return left  
        return s