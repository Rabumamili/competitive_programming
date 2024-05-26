class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        sup_set = set(supplies)
        g = defaultdict(list)
        indeg = defaultdict(int)
        
        for i, r in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in sup_set:
                    g[ing].append(r)
                    indeg[r] += 1
        
        q = deque()
        
        for r in recipes:
            if indeg[r] == 0:
                q.append(r)
        
        creatable = []
        
        while q:
            cur = q.popleft()
            creatable.append(cur)
            for neigh in g[cur]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
        
        return creatable
