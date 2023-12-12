class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        res  = set(fronts + backs)
        for i in range(len(backs)):
            if fronts[i]==backs[i] and fronts[i] in res:
                res.remove(fronts[i])
                
        if len(res)==0:
            return 0
        return min(res)