
class Solution:
    def balancedString(self, s: str) -> int:
        c = defaultdict(int)
        
        for i in range(len(s)):
            c[s[i]] += 1
      
        b = len(s) // 4
        minim= len(s)
        l = 0
        
        for i in range(len(s)):
            c[s[i]] -= 1

            while (l < len(s) and c["Q"] <= b and c["W"] <= b and c["E"] <= b and c["R"] <= b):
                minim = min(minim, i - l + 1)
                c[s[l]] += 1
                l += 1
        
        return minim
