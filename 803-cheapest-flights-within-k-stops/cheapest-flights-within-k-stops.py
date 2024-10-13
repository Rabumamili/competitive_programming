class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
           
        graph = {i: [] for i in range(n)}
        for u, v, cost in flights:
            graph[u].append((v, cost))

        heap = [(0, src, 0)]  
        best = {}  
        
        while heap:
            price, city, stops = heapq.heappop(heap)
          
            if city == dst:
                return price
           
            if stops > k:
                continue
           
            for neighbor, cost in graph[city]:
                new_cost = price + cost
                if (neighbor, stops) not in best or new_cost < best[(neighbor, stops)]:
                    best[(neighbor, stops)] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, stops + 1))
        
        return -1