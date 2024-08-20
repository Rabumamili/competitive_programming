class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        
        def dp(i, M):
            if i == n:
                return 0
            if 2 * M >= n - i:
                return suffix_sum[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0
            for X in range(1, 2 * M + 1):
                if i + X <= n:
                    best = max(best, suffix_sum[i] - dp(i + X, max(M, X)))

            memo[(i, M)] = best
            return best

        return dp(0, 1)