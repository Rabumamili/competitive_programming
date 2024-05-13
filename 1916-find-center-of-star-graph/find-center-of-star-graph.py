class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = {}
    
        
        for edge in edges:
            u, v = edge
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1
      
        for node, deg in degree.items():
            if deg == len(edges):
                return node
       