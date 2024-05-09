class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        available = []
        idx = 0
        for i in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(available, -projects[idx][1])
                idx += 1

            if available:
                w -= heapq.heappop(available)
            else:
                break

        return w