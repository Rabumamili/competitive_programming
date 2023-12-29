class Solution:
    def smallestNumber(self, num: int) -> int:
        mystrng = str(num)
        if num ==0:
            return 0
        if num >0:
            digits= sorted(mystrng)

            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int( "".join(digits))
        else:
            digits = sorted(mystrng[1:], reverse = True)
            return int("".join(digits)) *-1
        

        
