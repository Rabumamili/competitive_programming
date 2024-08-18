class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize the ugly number list with the first ugly number
        ugly = [1]
        p2 = p3 = p5 = 0
        
        # Continue generating ugly numbers until we reach the nth one
        while len(ugly) < n:
 
            next_ugly_2 = ugly[p2] * 2
            next_ugly_3 = ugly[p3] * 3
            next_ugly_5 = ugly[p5] * 5
            next_ugly = min(next_ugly_2, next_ugly_3, next_ugly_5)
            ugly.append(next_ugly)
            
            # Increment the corresponding pointer
            if next_ugly == next_ugly_2:
                p2 += 1
            if next_ugly == next_ugly_3:
                p3 += 1
            if next_ugly == next_ugly_5:
                p5 += 1
        return ugly[n-1]