class Solution:
    def smallestValue(self, n: int) -> int:
        def sumof(a, seen):
            sums = 0
            d = 2
            while d*d <= a:
                while a % d == 0:
                    a = a // d
                    sums += d
                d += 1
            if a > 1:
                sums += a
            print(seen)
            if sums == a or sums in seen:  
                return sums
            else:
                seen.add(sums)   
                return sumof(sums, seen)
             
        return sumof(n, set())   
