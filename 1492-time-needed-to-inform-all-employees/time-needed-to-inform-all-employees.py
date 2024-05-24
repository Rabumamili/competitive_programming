class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
            
        tree = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)
        
        
        def dfs(node):
            if node not in tree:
                return 0
            max_time = 0
            for subordinate in tree[node]:
                max_time = max(max_time, dfs(subordinate))
            return max_time + informTime[node]
        
        
        return dfs(headID)
    