class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
            
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
         
        queue = deque([1])
        visited = set()
        min_score = float('inf')
        
        while queue:
            city = queue.popleft()
            for neighbor, distance in graph[city]:
                if neighbor not in visited:
                    min_score = min(min_score, distance)
                    queue.append(neighbor)
            visited.add(city)
        
        return min_score