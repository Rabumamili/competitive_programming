class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def bfs(r, c):
            queue = deque()
            seen.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows)and nc in range(cols) and grid[nr][nc] == "1" and ((nr, nc)) not in seen:
                       queue.append((nr, nc ))
                       seen.add((nr, nc))
                
               
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1" and (r,c) not in seen:
                    ans +=1
                    bfs(r,c)
                         
        return ans