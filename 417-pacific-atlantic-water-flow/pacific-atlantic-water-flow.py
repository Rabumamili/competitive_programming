class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      

        m, n = len(heights), len(heights[0])

        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        def dfs(r, c, reach):
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            reach[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not reach[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reach)

        # Perform DFS from the Pacific Ocean's edges
        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n - 1, atl)
        for j in range(n):
            dfs(0, j, pac)
            dfs(m - 1, j, atl)

        # Find all cells that can reach both oceans
        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        
        return res