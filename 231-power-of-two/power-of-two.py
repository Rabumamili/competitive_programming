class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while n !=1:
            n = n/2
            if n%2 and n != 1:
                return False
        return True
