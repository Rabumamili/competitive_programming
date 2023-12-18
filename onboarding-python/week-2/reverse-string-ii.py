class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        s = list(s)
        i = 0

        while i < len(s):
            s[i:i+k] = s[i:i+k][::-1]
            i += 2 * k

        return ''.join(s)