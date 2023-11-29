class Solution:
    def isPalindrome(self, x: int) -> bool:
        num1= list(str(x))
        num2= list(str(x))
        num2.reverse()
        if num2==num1:
             return True
        else:
            return  False
        