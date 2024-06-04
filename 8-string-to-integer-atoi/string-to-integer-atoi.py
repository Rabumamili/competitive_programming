class Solution:
    def myAtoi(self, s: str) -> int:
        
        maxi = 2**31 - 1
        mini = -2**31
         
        i, n, sign, result = 0, len(s), 1, 0
       
        while i < n and s[i] == ' ':
            i += 1
     
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > (maxi - digit) // 10:
                return mini if sign == -1 else maxi
            
            result = result * 10 + digit
            i += 1
        return sign * result
