class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        R = len(grid)
        C = len(grid[0])
        visited = {(i, j) for i in range(R) for j in range(C) if grid[i][j] <= 0}

        def catch_fish(i, j):
            q = deque()
            fish = grid[i][j]
            visited.add((i, j))
            q.append((i, j))
            while q:
                cr, cc = q.popleft()
                for dr, dc in dirs:
                    r, c = cr + dr, cc + dc
                    if (r, c) not in visited and 0 <= r < R and 0 <= c < C and grid[r][c] > 0:
                        fish += grid[r][c]
                        visited.add((r, c))
                        q.append((r, c))
            return fish

        max_fish = 0
        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and grid[i][j] > 0:
                    fish_count = catch_fish(i, j)
                    max_fish = max(max_fish, fish_count)
        return max_fish
