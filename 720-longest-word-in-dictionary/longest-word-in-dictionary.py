class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()   
        buildable = set([""])   
        longest = ""

        for word in words:
            
            if word[:-1] in buildable:
                buildable.add(word)
                if len(word) > len(longest):
                    longest = word
        
        return longest