class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = max(days) + 1
        travel = set(days)
        memo = {}
        def dp(n):
            if n <= 0:
                return 0
            if n in memo:
                return memo[n]
            if n not in travel:
                memo[n] = dp(n-1)
            else:
                memo[n] = min(dp(n-1) + costs[0], dp(n-7) + costs[1], dp(n-30)+ costs[2])
            return memo[n]
        return dp(max_day -1)
            
 