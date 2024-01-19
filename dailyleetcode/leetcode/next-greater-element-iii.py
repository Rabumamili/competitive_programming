class Solution:
    def nextGreaterElement(self, n: int) -> int:
    
        
        digits = list(str(n))
        
  
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
         
        if i == -1:
            return -1
       
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
         
        digits[i], digits[j] = digits[j], digits[i]
         
        digits[i+1:] = sorted(digits[i+1:])
        
        new_num = int(''.join(digits))
        
        if new_num > 2**31 - 1:
            return -1
        
        
        return new_num 