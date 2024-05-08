class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = 0
        right = len(text)-1
        lef = ""
        righ = ""
        res = 0
        while left <len(text) and right > -1:
            lef += text[left]
            righ =  text[right] + righ
            if lef == righ:
                res += 1
                lef = righ = ""
            left += 1
            right -= 1
        return res 
            



        