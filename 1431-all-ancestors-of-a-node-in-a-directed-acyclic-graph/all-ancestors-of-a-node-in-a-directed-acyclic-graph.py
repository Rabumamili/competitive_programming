class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(n)]

        indegree = [0 for i in range(n)]
        graph = defaultdict(list)
        queue = deque()
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()

            for nbr in graph[curr]:
                ans[nbr].append(curr)
                if ans[curr]:
                    ans[nbr].extend(ans[curr])
                ans[nbr] = sorted(list(set(ans[nbr])))
                indegree[nbr] -= 1
                
                if indegree[nbr] == 0:
                    queue.append(nbr)
                    
        return ans