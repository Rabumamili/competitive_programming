class Solution:
    def partitionString(self, s: str) -> int:
        
        
        count = 1
        chars = set()
        
        for c in s:
            if c in chars:
                count += 1
                chars = set()
            
            chars.add(c)
        
        return count