from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = Counter(s)
        freq_t = Counter(t)

        diff = freq_s - freq_t
        return sum(diff.values())