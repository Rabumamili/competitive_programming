class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if rootX < rootY:
                self.parent[rootY] = rootX
            else:
                self.parent[rootX] = rootY
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
    
        for c in range(ord('a'), ord('z') + 1):
            uf.add(chr(c))
        
        for a, b in zip(s1, s2):
            uf.union(a, b)
        
        smallest_equiv = {chr(c): chr(c) for c in range(ord('a'), ord('z') + 1)}
        
        for c in range(ord('a'), ord('z') + 1):
            root = uf.find(chr(c))
            if root < smallest_equiv[root]:
                smallest_equiv[root] = root
            smallest_equiv[chr(c)] = smallest_equiv[root]
        
        result = []
        for char in baseStr:
            result.append(smallest_equiv[char])
        
        return ''.join(result)

