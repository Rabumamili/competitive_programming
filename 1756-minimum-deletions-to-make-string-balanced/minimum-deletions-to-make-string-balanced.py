class Solution:
    def minimumDeletions(self, s: str) -> int:
            
        n = len(s)
        b_count = [0] * n
        a_count = [0] * n
        
        # Count 'b's before each index
        b = 0
        for i in range(n):
            if s[i] == 'b':
                b += 1
            b_count[i] = b  
        
        # Count 'a's after each index
        a = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                a += 1
            a_count [i] = a
        
        #  minimum number of deletions needed
        op = float('inf')
        for i in range(n):
            op = min(op, b_count[i] + a_count[i])
        
        return op -1
 