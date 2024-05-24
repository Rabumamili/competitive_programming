class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
   
        m, n = len(grid), len(grid[0])
        start_x, start_y = 0, 0
        empty_count = 0
        
        # Find the starting point and count the number of empty squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                if grid[i][j] != -1:
                    empty_count += 1

        def dfs(x, y, count):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if count == empty_count else 0
            temp = grid[x][y]
            grid[x][y] = -1
            paths = dfs(x+1, y, count+1) + dfs(x-1, y, count+1) + dfs(x, y+1, count+1) + dfs(x, y-1, count+1)
             
            grid[x][y] = temp
            return paths
        return dfs(start_x, start_y, 1)

        

  