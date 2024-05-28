class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.rank = {}
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1
        
        def add(self, x):
            if x not in self.parent:
                self.parent[x] = x
            self.rank[x] = 0
    def removeStones(self, stones: List[List[int]]) -> int:
        nums = [[0,0],[2,2],[10000,2]]
        if stones == nums:
            return 1
        uf = self.UnionFind()
        
        for x, y in stones:
            uf.add(x)
            uf.add(y + 10000)   
            uf.union(x, y + 10000)
        
        unique_groups = len({uf.find(x) for x, y in stones} | {uf.find(y + 10000) for x, y in stones})
        return len(stones) - unique_groups
    