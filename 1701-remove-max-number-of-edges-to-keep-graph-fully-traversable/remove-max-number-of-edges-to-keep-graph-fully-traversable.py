from typing import List

class UnionFind:
    def __init__(self, n):
        self.count = n                             # number of disjoint sets
        self.parent = [i for i in range(n + 1)]    # parent of given nodes
        self.rank = [1] * (n + 1)                   

    def find(self, n1):
        curr = n1
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]  
            curr = self.parent[curr]

        return curr

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        # union by rank
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
 
        self.count -= 1
        return True
 
    def isConnected(self):
        return self.count == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        count = 0          
        for t, src, des in edges:
            if t == 3 and (alice.find(src) != alice.find(des) or bob.find(src) != bob.find(des)):
                count += 1
                alice.union(src, des)
                bob.union(src, des)

        for t, src, des in edges:
            # alice type
            if t == 1 and alice.find(src) != alice.find(des):
                count += 1
                alice.union(src, des)   
            # bob type
            elif t == 2 and bob.find(src) != bob.find(des):
                count += 1
                bob.union(src, des)  

        m = len(edges)
        if alice.isConnected() and bob.isConnected():
            return m - count
        return -1
