class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    
        meetings.sort()
 
        free_rms = [i for i in range(n)]
        heapq.heapify(free_rms)
    
        on_mtg = []
        
        rm_use = [0] * n
        
        for st, en in meetings:
             
            while on_mtg and on_mtg[0][0] <= st:
                end, rm = heapq.heappop(on_mtg)
                heapq.heappush(free_rms, rm)
          
            if free_rms:
                rm = heapq.heappop(free_rms)
                heapq.heappush(on_mtg, (en, rm))
            else:
                
                end, rm = heapq.heappop(on_mtg)
                newend = end + (en - st)
                heapq.heappush(on_mtg, (newend, rm))
            
             
            rm_use[rm] += 1
        
        max_mtg = max(rm_use)
        for i in range(n):
            if rm_use[i] == max_mtg:
                return i