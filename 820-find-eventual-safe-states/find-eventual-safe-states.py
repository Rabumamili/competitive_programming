class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1  # Mark node as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2  # Mark node as safe
            return True
        
        n = len(graph)
        state = [0] * n
        safe_nodes = []
        
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        
        return sorted(safe_nodes)
