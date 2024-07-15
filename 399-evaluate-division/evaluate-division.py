class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        for (u, v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1 / value
       
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            queue = deque([(start, 1.0)])
            visited = set()
            
            while queue:
                current, cur_product = queue.popleft()
                if current == end:
                    return cur_product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, cur_product * value))
            
            return -1.0

        results = []
        for start, end in queries:
            result = bfs(start, end)
            results.append(result)
        
        return results
