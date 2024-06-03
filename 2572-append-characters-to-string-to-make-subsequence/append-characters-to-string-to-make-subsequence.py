class Solution:
    def appendCharacters(self, s: str, t: str) -> int: 
        s_idx, t_idx = 0, 0
        s_len, t_len = len(s), len(t)
        while s_idx < s_len and t_idx < t_len:
            if s[s_idx] == t[t_idx]:
                t_idx += 1
            s_idx += 1
        return t_len - t_idx
    