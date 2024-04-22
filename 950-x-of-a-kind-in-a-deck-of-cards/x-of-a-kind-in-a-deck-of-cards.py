class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
    
        count = Counter(deck)
        gcd_val = None
        
        for val in count.values():
            if gcd_val is None:
                gcd_val = val
            else:
                gcd_val = gcd(gcd_val, val)
                
        return gcd_val > 1
            
            