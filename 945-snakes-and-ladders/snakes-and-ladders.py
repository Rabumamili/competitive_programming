
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        lst = [0]
        for r in range(n):
            if r % 2 == 0:
                lst += board[n - r - 1]
            else:
                lst += board[n - r - 1][::-1]
        
        queue = deque([(1, 0)])  # (position, steps)
        visited = set([1])
        
        while queue:
            position, steps = queue.popleft()
            
            if position == n ** 2:
                return steps
            
            for i in range(1, 7):
                new_position = position + i
                
                if new_position > n ** 2:
                    break
                
                if lst[new_position] != -1:
                    new_position = lst[new_position]
                
                if new_position not in visited:
                    visited.add(new_position)
                    queue.append((new_position, steps + 1))
        
        return -1