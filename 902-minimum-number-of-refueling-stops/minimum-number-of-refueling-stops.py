class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [0] * (n + 1)
        dp[0] = startFuel
        
        for i, (position, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= position:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        
        for i in range(n + 1):
            if dp[i] >= target:
                return i
        
        return -1