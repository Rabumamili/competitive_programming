class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n = 1
        for num in nums:
            n *= num
            
        def primefactors(n):
            factors = []
            divisor = 2
    
            while n > 1:
                 
                while n % divisor == 0:
                    if len(factors)==0 or factors[-1] != divisor:

                        factors.append(divisor)
                    n //= divisor
                 
                divisor += 1
            
            return len(factors)
        return primefactors(n)