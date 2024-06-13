class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
          return 1
    
        t_others = [0] * (n + 1)
        t_by_others = [0] * (n + 1)
        
        for a, b in trust:
            t_others[a] += 1
            t_by_others[b] += 1
        
        for i in range(1, n + 1):
            if t_others[i] == 0 and t_by_others[i] == n - 1:
                return i
        
        return -1