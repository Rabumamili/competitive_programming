class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        
        magicstr = [1, 2, 2]
        i = 2
        
        while len(magicstr) < n:
            count = magicstr[i]
            value = 3 - magicstr[-1]
            magicstr.extend([value] * count)
            i += 1
        
        ones = magicstr[:n].count(1)
        return ones