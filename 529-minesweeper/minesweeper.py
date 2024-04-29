class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(board, i, j):
            if board[i][j] == 'M':
                board[i][j] = 'X'   
                return
            if board[i][j] != 'E':
                return
 
            count = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                        count += 1

            if count > 0:
                board[i][j] = str(count)   
            else:
                board[i][j] = 'B'   
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n:
                            dfs(board, x, y)

        m, n = len(board), len(board[0])
        click_r, click_c = click
        dfs(board, click_r, click_c)
        return board