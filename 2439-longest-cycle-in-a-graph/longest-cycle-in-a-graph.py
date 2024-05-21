class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        v = [0] * len(edges)
        p = [0] * len(edges)
        c = []

        def dfs(node):
            v[node] = 1
            c.append(node)
            p[node] = 1

            m = -1
            n = edges[node]

            if n != -1 and v[n] == 0:
                m = max(dfs(n), m)
            elif p[n] == 1 and n != -1:
                i = c.index(n)
                p[node] = 0
                return len(c[i:])
            p[node] = 0
            return m

        m = -1
        for i in range(len(edges)):
            if v[i] == 0:
                l = dfs(i)
                m = max(l, m)
        return m   