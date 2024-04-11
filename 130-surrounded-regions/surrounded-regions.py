class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        directions = [(0,1), (0,-1), (-1, 0), (1,0)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m


        def dfs(r,c):
            if board[r][c] == "X" or not inbound(r,c):
                return 

            visited[r][c] = True
            board[r][c] = "Y"
            for i,j in directions: 
                nr, nc = r + i, c + j
                if inbound(nr, nc):
                    if not visited[nr][nc] and board[nr][nc] == "O":
                        dfs(nr, nc)
            

        for r in range(n):
            for c in range(m):
                if r == 0 or c == 0 or r == n -1 or c == m - 1:
                    if not visited[r][c] and board[r][c] == "O":
                        dfs(r,c)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "Y":
                    board[i][j] = "O"