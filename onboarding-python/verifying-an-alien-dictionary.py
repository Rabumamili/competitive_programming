class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
    
        sorted_words = sorted(words, key=lambda word: [order.index(c) for c in word])
        if words == sorted_words:
            return True
        else:
            return False