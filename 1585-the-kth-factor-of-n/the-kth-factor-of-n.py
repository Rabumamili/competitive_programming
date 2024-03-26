class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        for i in range(1, int((n**0.5)+1)):
            if n %i==0:
                factors.append(i)
                if n//i != i:
                    factors.append(n//i)
        factors.sort()
        if len(factors)< k:
            return -1
        
        return factors[k-1]
        