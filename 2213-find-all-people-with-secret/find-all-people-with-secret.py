class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        
        i = 0
        while i < len(meetings):
            current_time = meetings[i][2]
            group = []
            
            while i < len(meetings) and meetings[i][2] == current_time:
                x, y, time = meetings[i]
                group.append((x, y))
                i += 1
            
            for x, y in group:
                uf.union(x, y)
            
            for x, y in group:
                if uf.find(x) != uf.find(0):
                    uf.parent[x] = x
                    uf.parent[y] = y
        ans = []
        for i in range(n):
            if uf.find(i) == uf.find(0):
                ans.append(i)
        
        return  ans