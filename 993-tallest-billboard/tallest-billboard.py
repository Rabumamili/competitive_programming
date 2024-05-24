class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        dp = {0: 0}
        for rod in rods:
            cur = dict(dp)  # Make a copy of current state
            for d in cur:
                dp[d + rod] = max(dp.get(d + rod, 0), cur[d])
                dp[abs(d - rod)] = max(dp.get(abs(d - rod), 0), cur[d] + min(d, rod))
        
        return dp[0]
 