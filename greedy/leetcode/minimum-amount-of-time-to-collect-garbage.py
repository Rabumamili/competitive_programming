class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g = m = p = False   
        time = 0  
        while len(travel):
            t = travel.pop()   
            s = garbage.pop()  
            if sum([g, m, p]) < 3:
                if 'G' in s:
                    g = True
                if 'M' in s:
                    m = True
                if 'P' in s:
                    p = True
                        
            time += sum([g, m, p]) * t + len(s)
        time = time + len(garbage[0])  
        
        return time