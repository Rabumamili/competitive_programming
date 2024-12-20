class Solution:
    def countVowels(self, word: str) -> int:
        counts = 0
        n = len(word)
        s = "aeiou"
        for i in range(n):
            if word[i] in s:
                counts += (i+1)*(n-i)
                
        return counts