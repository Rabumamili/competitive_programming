class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(node):
            component.append(node)
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        n = len(s)
        graph = [[] for _ in range(n)]
        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        visited = [False] * n
        result = list(s)
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i)
                component_chars = sorted([s[j] for j in component])
                component.sort()
                for k in range(len(component)):
                    result[component[k]] = component_chars[k]

        return "".join(result)