class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]  
        heapq.heapify(heap)
        while k >0:
            maxi = -heapq.heappop(heap)
            nw = maxi - (maxi//2)
            heapq.heappush(heap, -nw)
            k -= 1
        return -sum(heap)
        
        