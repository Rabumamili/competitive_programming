class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        # Step 2: Find all connected components
        def dfs(node):
            stack = [node]
            size = 0
            while stack:
                curr = stack.pop()
                if not visited[curr]:
                    visited[curr] = True
                    size += 1
                    for neighbor in g[curr]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            return size

        visited = [False] * n
        comp_sizes = []

        for i in range(n):
            if not visited[i]:
                comp_size = dfs(i)
                comp_sizes.append(comp_size)
        
        total = n * (n - 1) // 2
        reach = sum(size * (size - 1) // 2 for size in comp_sizes)
        ans = total - reach
        
        return ans