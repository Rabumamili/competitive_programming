class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
     
        mask_count = {0: 1}
        curr = 0
        count = 0
        
        for char in word:
            curr ^= 1 << (ord(char) - ord('a'))
            count += mask_count.get(curr, 0)
            
            for i in range(10):
                onebit = curr ^ (1 << i)
                count += mask_count.get(onebit, 0)
            
            mask_count[curr] = mask_count.get(curr, 0) + 1
        
        return count