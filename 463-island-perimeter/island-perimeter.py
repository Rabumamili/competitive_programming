class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        seen = set()

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))


        def dfs(grid, row, col):
            nonlocal ans
         
            if grid[row][col] == 0:
                ans += 1
                return

            
            seen.add((row, col))
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change


                if (new_row, new_col) not in seen:
                    if inbound(new_row, new_col):
                        dfs(grid, new_row, new_col)

                    else:
                        ans += 1


 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(grid, row, col)
                    return ans