class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        sums, performance = 0, 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            sums += spd

            if len(speed_heap) > k:
                sums -= heapq.heappop(speed_heap)

            performance = max(performance, sums * eff)

        return performance % (10**9 + 7)