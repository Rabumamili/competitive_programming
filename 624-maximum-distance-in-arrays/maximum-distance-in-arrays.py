class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
          
        g_min = arrays[0][0]
        g_max = arrays[0][-1]
        max_dist = 0
        
     
        for i in range(1, len(arrays)):
            curr = arrays[i]
            max_dist = max(max_dist, abs(g_max - curr[0]), abs(curr[-1] - g_min))
            g_min = min(g_min, curr[0])
            g_max = max(g_max, curr[-1])
        
        return max_dist