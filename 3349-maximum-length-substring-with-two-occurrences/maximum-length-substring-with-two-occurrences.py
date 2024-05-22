class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        maxi = 1
        right = 0
        counts ={}
        while right < n:
            counts[s[right]] = counts.get(s[right], 0) +1
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]

                left += 1
            maxi = max(maxi, right - left +1)
            right += 1
        return maxi