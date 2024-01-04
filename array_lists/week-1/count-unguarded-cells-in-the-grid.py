from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        G=set()
        M=[[0]*n for _ in range(m)]
        
        for i, j in walls:
            M[i][j] = 1
            
        for i, j in guards:
            M[i][j] = 2
        
        for i, j in guards:
            j1 = j - 1
            while j1 >= 0:
                if M[i][j1] in (1, 2):
                    break
                G.add((i, j1))
                j1 -= 1
            
            j1 = j + 1
            while j1 < n:
                if M[i][j1] in (1, 2):
                    break
                G.add((i, j1))
                j1 += 1
            
            i1 = i - 1
            while i1 >= 0:
                if M[i1][j] in (1, 2):
                    break
                G.add((i1, j))
                i1 -= 1
            
            i1 = i + 1
            while i1 < m:
                if M[i1][j] in (1, 2):
                    break
                G.add((i1, j))
                i1 += 1
        
        return m * n - len(guards) - len(walls) - len(G)