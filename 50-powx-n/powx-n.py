class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0 if n > 0 else float('inf')  

        result = 1
        curr = abs(n)
        while curr > 0:
            if curr % 2 == 1:   
                result *= x
            x *= x   
            curr //= 2   

        return result if n > 0 else 1 / result

