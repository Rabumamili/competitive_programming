class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(index, current):
            if index == len(s):
                result.append(current)
                return
            
            if s[index].isalpha():
                backtrack(index + 1, current + s[index].lower())
                backtrack(index + 1, current + s[index].upper())
            else:
                backtrack(index + 1, current + s[index])
    
        result = []
        backtrack(0, "")
        return result