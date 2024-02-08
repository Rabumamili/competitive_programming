 
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = [0]*len(word)
        rem =0
        for i in range(len(word)):
            rem = (rem *10 + (int(word[i])))% m
            if rem ==0:
                ans[i] = 1
        return ans