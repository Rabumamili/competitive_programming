class Solution:
    def countPrimes(self, n: int) -> int:
            
        prime = [True for _ in range(n )]
        p = 2
        while p*p < n:
            # If prime[p] is not changed, then it is a prime
            if prime[p]:
                # Update all multiples of p
                for i in range(p*p, n , p):
                    prime[i] = False
            p += 1

        primes = []
        for p in range(2, n ):
            if prime[p]:
                primes.append(p)
        return len(primes)