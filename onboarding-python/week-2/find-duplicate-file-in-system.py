class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        direct = defaultdict(list)

        for p in paths:
            s = p.split()
            path = s[0]
            for i in range(1, len(s)):
                files = s[i].split('(')
                direct[files[1][:-1]].append(path + '/' + files[0])

        return [v for v in direct.values() if len(v) > 1]