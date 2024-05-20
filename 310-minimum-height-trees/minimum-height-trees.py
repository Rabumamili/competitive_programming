class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        leaves = deque([i for i in range(n) if len(adj[i]) == 1])
        remaining = n
        
        while remaining > 2:
            size = len(leaves)
            remaining -= size
            
            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)
    