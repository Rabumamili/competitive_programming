class Solution:
    def countVowels(self, word: str) -> int:
        counts = 0
        s = "aeiou"
        n = len(word)
        for i in range(n):
            if word[i] in s:
                counts  += (i+1)*(n-i)
        return counts