class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo=  {}
        num = max(nums)
        freq = Counter(nums)
        def dp(n):
            if n <= 0:
                return 0
            if n not in memo:
                memo[n] = max(n*freq[n] + dp(n-2), dp(n-1))

            return memo[n]

        return(dp(num))