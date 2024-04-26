class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        disjoint_set = DisjointSet(n)
        
        
        queries = sorted([(a, b, d, i) for i, (a, b, d) in enumerate(queries)], key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
         
        ans = [False] * len(queries)
        s = 0  
         
        for k in range(len(queries)):
            a, b, d, i = queries[k]
            while s < len(edgeList) and edgeList[s][2] < d:
                x, y, _ = edgeList[s]
                disjoint_set.union(x, y)
                s += 1
            
            ans[i] = disjoint_set.find(a) == disjoint_set.find(b)
        
        return ans
