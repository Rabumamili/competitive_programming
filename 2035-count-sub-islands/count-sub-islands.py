class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid2[0])
    
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid2[r][c] == 0:
                return True
            grid2[r][c] = 0   
            island = True

            if grid1[r][c] == 0:
                island = False
            
            # Explore all 4 directions
            island &= dfs(r+1, c)
            island &= dfs(r-1, c)
            island &= dfs(r, c+1)
            island &= dfs(r, c-1)
            
            return island
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        
        return count