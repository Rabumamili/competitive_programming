class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        max_profit = 0
        ans = 0
        i = 0
        
        for able in worker:
            while i < len(jobs) and able >= jobs[i][0]:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            ans += max_profit
        
        return ans