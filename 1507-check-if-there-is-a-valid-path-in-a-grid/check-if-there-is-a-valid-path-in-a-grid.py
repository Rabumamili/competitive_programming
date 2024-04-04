class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        directions =  {1:[(0, -1),(0, 1)], 2:[(-1, 0), (1, 0)],3: [(0,-1),(1,0)],4: [(0,1),(1,0)],5: [(0,-1),(-1,0)],6: [(0,1),(-1,0)]}
        destination = (len(grid)-1, len(grid[0]) -1)
        rows = len(grid)
        cols = len(grid[0])

        def inbound(row, col):
            return 0 <=row <rows and 0 <= col < cols
        
        
        def dfs(row, col):

            if (row, col) == destination:
                return True

            for row_change, col_change in directions[grid[row][col]]:
                new_row= row + row_change
                new_col = col + col_change
                
                if (inbound(new_row, new_col) and
                (new_row, new_col) not in seen and
                (-row_change, -col_change) in
                directions[grid[new_row][new_col]]):

                    seen.add((new_row, new_col))
                    found = dfs(new_row, new_col)
                    
                    if found:
                        return True
            return False 

        seen = set([(0, 0)])
        return dfs(0,0)
    
            
