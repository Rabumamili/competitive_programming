class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n==0:
                return 1
            if x==0:
                return 0
            ans = pow(x, n//2)
            ans = ans*ans
            return x*ans if n%2 else ans
        ans = pow(x, abs(n))
        return ans if n>0 else 1/ans

            
         