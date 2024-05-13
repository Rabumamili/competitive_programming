class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n

        def dp(i):
            if i == n:
                return 0
            if memo[i] == 0:
                for j in range(i + 1, n):
                    if nums[j] > nums[i]:
                        memo[i] = max(memo[i], 1 + dp(j))
                if memo[i] == 0: 
                    memo[i] = 1
            return memo[i]

        ans = 0
        for i in range(n):
            ans = max(ans, dp(i))
        return ans
