class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
       
        maxHeap = [(-1.0, start_node)]  # (negative probability, node) because heapq is a min-heap by default
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        
        # Step 3: Dijkstra's-like algorithm to maximize probability
        while maxHeap:
            currProb, node = heapq.heappop(maxHeap)
            currProb = -currProb  # convert back to positive
            
            # If we reach the end node, return the probability
            if node == end_node:
                return currProb
            
            for neighbor, edgeProb in graph[node]:
                newProb = currProb * edgeProb
                if newProb > maxProb[neighbor]:
                    maxProb[neighbor] = newProb
                    heapq.heappush(maxHeap, (-newProb, neighbor))
        return 0.0