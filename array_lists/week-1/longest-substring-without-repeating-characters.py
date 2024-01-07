class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left =0
        result = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[r])
            result = max(result, r -left +1)
        return result
