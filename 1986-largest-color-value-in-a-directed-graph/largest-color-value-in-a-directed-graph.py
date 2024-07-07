class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = defaultdict(list)
        in_deg = [0] * n
        
        for u, v in edges:
            g[u].append(v)
            in_deg[v] += 1
        
         
        q = deque([i for i in range(n) if in_deg[i] == 0])
        topo = []
        
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in g[node]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)
        
        if len(topo) < n:
            return -1  # Cycle detected
        
        # Initialize the dp table
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1
        
         
        for node in topo:
            for nei in g[node]:
                for c in range(26):
                    dp[nei][c] = max(dp[nei][c], dp[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0))
      
        res = max(max(row) for row in dp)
        
        return res