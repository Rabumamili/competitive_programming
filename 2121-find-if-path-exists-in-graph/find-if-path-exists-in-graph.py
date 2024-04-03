class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs (node, seen):
            if node == destination:
                return True

            seen.add(node)

            for neighbour in graph[node]:
                if neighbour not in seen:
                    found = dfs(neighbour, seen)
                    if found:
                        return True
            
            return False
        
        # build the graph
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        print(graph)
        
        seen = set()
        return dfs(source, seen)