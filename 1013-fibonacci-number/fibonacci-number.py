class Solution:
    def fib(self, n: int) -> int:
        def fb(n,memo={}):
            if n in memo:
                return memo[n]
            if n<=0:
                return 0
            if n<=2:
                return 1
            memo[n]=fb(n-1,memo)+fb(n-2,memo)
            return memo[n]

        return fb(n)