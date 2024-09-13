class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        count = 0
        for word in words:
             if all(char in allowedSet for char in word):
                count +=1
        return count