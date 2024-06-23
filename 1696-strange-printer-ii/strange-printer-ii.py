class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        bounds = {}

        # Identify the boundaries for each color
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c not in bounds:
                    bounds[c] = [i, i, j, j]  # [min_row, max_row, min_col, max_col]
                else:
                    bounds[c][0] = min(bounds[c][0], i)
                    bounds[c][1] = max(bounds[c][1], i)
                    bounds[c][2] = min(bounds[c][2], j)
                    bounds[c][3] = max(bounds[c][3], j)
        
        # Check if we can print each color without reusing it
        printed = set()
        
        def canPrint(c):
            min_r, max_r, min_c, max_c = bounds[c]
            for i in range(min_r, max_r + 1):
                for j in range(min_c, max_c + 1):
                    if grid[i][j] != c and grid[i][j] not in printed:
                        return False
            return True

        while bounds:
            progress = False
            for c in list(bounds.keys()):
                if canPrint(c):
                    printed.add(c)
                    del bounds[c]
                    progress = True
            if not progress:
                return False

        return True
    