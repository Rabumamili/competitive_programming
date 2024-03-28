class Solution:
 
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = [True for i in range(n+1)]
        primes[0] = primes[1] = False
        
        i = 2
        while i * i <= n:
            if primes[i]:
                j = i * i
                while j <= n:
                    primes[j] = False
                    j += i
            i += 1
        
        nums = set([i for i in range(2, n+1) if primes[i]])
        ans = []
        
        for num in nums: 
            if (n - num) in nums and( n - num)>= num:
                ans.append([num, n - num])
        
        
        return sorted(ans)