
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if fresh == 0:
            return 0

        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        while len(q) > 0 and fresh > 0:
            for _ in range(len(q)):
                node = q.popleft()

                for i in range(len(direction)):
                    row, col = node
                    row += direction[i][0]
                    col += direction[i][1]

                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1:
                        q.append((row, col))
                        fresh -= 1
                        grid[row][col] = 2

            time += 1
        
        return time if fresh == 0 else -1
            
