class Solution:
    def countGoodNumbers(self, n: int) -> int:
    
        Mod = 10**9 +7
        def modPow(x: int, n: int) -> int:
            if n == 0:
                return 1
            if n & 1:
                return x * modPow(x, n - 1) % Mod
            return modPow(x * x % Mod, n // 2)

        return modPow(4 * 5, n // 2) * (5 if n & 1 else 1) % Mod