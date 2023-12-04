class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        b = "".join(word1)
        c = "".join(word2)
        if len(b)!=len(c):
            return False
        for i in range(len(b)):
            if b[i]!=c[i]:
                return False
        return True
