class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])  
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = []
    
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()

        uf = UnionFind(n)
        min_cost = 0
        edges_used = 0
        
        for dist, i, j in edges:
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                min_cost += dist
                edges_used += 1
                if edges_used == n - 1:
                    break
                    
        return min_cost
    