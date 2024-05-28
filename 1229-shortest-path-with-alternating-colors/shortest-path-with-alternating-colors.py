class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
     
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][0] = dist[0][1] = 0   
        queue = deque([(0, 0, 0), (0, 1, 0)])  
        
        while queue:
            node, color, d = queue.popleft()
            
            if color == 0: 
                for neighbor in blue_graph[node]:
                    if d + 1 < dist[neighbor][1]:
                        dist[neighbor][1] = d + 1
                        queue.append((neighbor, 1, d + 1))
            else:   
                for neighbor in red_graph[node]:
                    if d + 1 < dist[neighbor][0]:
                        dist[neighbor][0] = d + 1
                        queue.append((neighbor, 0, d + 1))
     
        answer = []
        for red_dist, blue_dist in dist:
            min_dist = min(red_dist, blue_dist)
            answer.append(min_dist if min_dist != float('inf') else -1)
        
        return answer
