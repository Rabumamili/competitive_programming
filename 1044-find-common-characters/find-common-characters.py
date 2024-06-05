class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
                
        common_count = Counter(words[0])
       
        for word in words[1:]:
            common_count &= Counter(word)

        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result