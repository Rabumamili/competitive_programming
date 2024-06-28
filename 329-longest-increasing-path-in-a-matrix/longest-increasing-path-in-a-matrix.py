class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(x, y):
            if memo[x][y] != -1:
                return memo[x][y]

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            max_length = 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    length = 1 + dfs(nx, ny)
                    max_length = max(max_length, length)

            memo[x][y] = max_length
            return max_length

        length = 0
        for i in range(m):
            for j in range(n):
                length = max(length, dfs(i, j))

        return length
