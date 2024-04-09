
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges_count = 0
        time = -1
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    oranges_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if oranges_count == 0:
            return 0

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        
        while len(q) > 0:
            print(len(q))
            for _ in range(len(q)):
                node = q.popleft()
                for i in range(len(dirs)):
                    row, col = node
                    row += dirs[i][0]
                    col += dirs[i][1]
                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1:
                        q.append((row, col))
                        oranges_count -= 1
                        grid[row][col] = 2
            time += 1
        
        if oranges_count == 0:
            return time
        else:
            return -1
            
