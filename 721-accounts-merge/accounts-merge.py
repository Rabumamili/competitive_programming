class Solution:
    def accountsMerge(self, accs: List[List[str]]) -> List[List[str]]:
        def find(x):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]

        def union(x, y):
            y = find(y)
            x = find(x)
            if x == y:
                return -1
            if sz[x] >= sz[y]:
                par[y] = par[x]
            else:
                par[x] = par[y]

        par = {i: i for i in range(len(accs))}
        sz = {i: 0 for i in range(len(accs))}
        num = set(range(len(accs)))

        for i in range(len(accs)):
            for e in accs[i][1:]:
                if e in par:
                    union(i, e)
                else:
                    par[e] = find(i)

        ans = defaultdict(list)
        for k in par:
            if k not in num:
                ans[find(k)].append(k)

        res = []
        for i in ans:
            tmp = [accs[i][0]] + sorted(ans[i])
            res.append(tmp)

        return res
