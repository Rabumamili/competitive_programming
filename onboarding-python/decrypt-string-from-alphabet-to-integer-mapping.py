class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans =""
        j = len(s)-1
        while j >= 0:
            if s[j]=="#":
                ans = ans + chr(int(s[j-2: j]) +96)
                j = j-3
            else:
                ans = ans + chr(int(s[j])+96)
                j -=1
        return ans[:: -1]