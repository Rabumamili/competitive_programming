class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for _ in range(right + 1)]
        primes[0] = primes[1] = False
        i = 2
        while i * i <= right:
            if primes[i]:
                j = i * i
                while j <= right:
                    primes[j] = False
                    j += i
            i += 1
        
         
        pair = None
        min_diff = float('inf')

        
        l = left
        r = left +1 
        while r <=right:
             
            if primes[l] and primes[r]:
                diff = r -l
                if diff < min_diff:
                    pair = (l, r)
                    min_diff = diff
                l += 1
            
            while not primes[l] and l < r:
                l +=1
                 
            r += 1
         
        if pair:
            return list(pair)
        else:
            return [-1, -1]