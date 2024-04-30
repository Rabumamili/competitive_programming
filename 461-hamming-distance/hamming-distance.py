class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
       xors = bin(x^y)
       #print(xors)
       return xors.count("1")