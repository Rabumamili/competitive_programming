class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        
        total, i, mid = 0, 0, len(costs) // 2
        while i < mid:
            total += costs[i][0] + costs[i+mid][1]
            i += 1
        
        return total