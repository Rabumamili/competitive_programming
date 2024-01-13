class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        words = list(word)
        start = 0
        end = word.index(ch)
        while start < end:
            words[start], words[end] =words[end],  words[start]
            start += 1
            end -= 1
        return "".join(words)

     

