class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        for v, u in richer:
            graph[u].append(v)

       
        ans = [0 for i in range(len(quiet))]

        def dfs(node):
            
            if node in visited:
                return

            visited.add(node)
            quietest = node
            for nbr in graph[node]:
                if nbr not in visited:
                    candidate = dfs(nbr)
                    if quiet[quietest] > quiet[candidate]:
                        quietest = candidate
        
            return  quietest

      
        for i in range(len(quiet)):
            visited = set()
            ans[i] = dfs(i)
            
            
            
       
        return ans



            
