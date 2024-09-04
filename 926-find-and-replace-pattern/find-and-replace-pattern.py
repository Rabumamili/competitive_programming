class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(w, p):
            w_map, p_map = {}, {}
            
            for wc, pc in zip(w, p):
                if wc not in w_map:
                    w_map[wc] = pc
                if pc not in p_map:
                    p_map[pc] = wc
                
                if w_map[wc] != pc or p_map[pc] != wc:
                    return False
            
            return True
    
        return [w for w in words if match(w, pattern)]