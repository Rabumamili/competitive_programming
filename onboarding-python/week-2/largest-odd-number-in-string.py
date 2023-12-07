class Solution:
    def largestOddNumber(self, num: str) -> str:
        index = len(num) - 1
    
        while index >= 0:
            if int(num[index]) % 2:
                return num[:index+1]
            index -= 1
        
        return ""
            