class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in roots:
                    return word[:i]
            return word
        
        words = sentence.split()
        replaced = [replace(word) for word in words]
 
        return ' '.join(replaced)

    