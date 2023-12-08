class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        prev = 0
        
        for space in spaces:
            result += s[prev:space] + " "
            prev = space
        
        result += s[prev:]
        
        return result
        