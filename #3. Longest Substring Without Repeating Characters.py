class Solution(object):
    def lengthOfLongestSubstring(self, s ) :
        b = {}
        size = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] not in b or b[s[right]] < left:
                b[s[right]] = right
                size = max(size, right-left + 1)
            else:
                left = b[s[right]] + 1
                b[s[right]] = right
            right += 1
        return size
