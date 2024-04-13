class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n  # Initialize all nodes with color -1 (unvisited)

        for node in range(n):
            if colors[node] == -1:  # If the node is unvisited
                colors[node] = 0  # Color it with 0
                queue = deque([node])

                while queue:
                    curr_node = queue.popleft()
                    for neighbor in graph[curr_node]:
                        if colors[neighbor] == -1:  # If neighbor is unvisited
                            colors[neighbor] = 1 - colors[curr_node]  # Assign opposite color to neighbor
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[curr_node]:  # Not bipartite
 
                            return False  
        return True   
