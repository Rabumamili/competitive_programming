class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        print(premap)

        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if not premap[crs]:
                return True
            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre): return False

            visit.remove(crs)
            premap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

