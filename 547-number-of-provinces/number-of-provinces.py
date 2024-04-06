class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[j][i]:
                    graph[i].append(j)

        res = 0
        visited = set()
        def dfs(i):
            
            visited.add(i)
            for neighbor in graph[i]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        
        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                dfs(i)
        return res
            
            


            