
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        d = defaultdict(int)
        for word in words:
            mask = 0
            for w in set(word):
                mask |= 1 << (ord(w) - ord('a'))
            d[mask] = max(d[mask], len(word))


        res = 0
        for x in d:
            for y in d:
                if x == y:
                    continue
                if not x & y:
                    res = max(res, d[x] * d[y])
        
        return res