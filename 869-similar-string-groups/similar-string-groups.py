class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = {i:i for i in strs}
        size = {i:0 for i in strs}
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            y = find(y)
            x = find(x)
            if x == y:
                return -1
            if size[x] >= size[y]:
                parent[y] = parent[x]
            else:
                parent[x] = parent[y]
        def similar(s1,s2):
            t = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    t += 1
                if t > 2:
                    return False
            return t == 2

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i],strs[j]):
                    union(strs[i],strs[j])
                     
        ans = set()
        for s in parent:
            ans.add(find(s))
        return len(ans)