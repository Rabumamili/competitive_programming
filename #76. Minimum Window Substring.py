class Solution(object):
    def minWindow(self, s, t):
        
         
        t_counter = Counter(t)

         
        left = 0
        min_window = ""
        min_length = float('inf')
        count = len(t)
        
        
        for right in range(len(s)):
             
            if t_counter[s[right]] > 0:
                count -= 1
            
             
            t_counter[s[right]] -= 1
            
            
            while count == 0:
                 
                if right - left + 1 < min_length:
                    min_window = s[left:right+1]
                    min_length = right - left + 1
                
               
                t_counter[s[left]] += 1
                if t_counter[s[left]] > 0:
                    count += 1
                left += 1
        
        return min_window
