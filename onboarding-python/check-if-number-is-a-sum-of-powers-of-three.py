class Solution(object):
    def checkPowersOfThree(self, n):
        
        flag= True
        while n>0:
            if n%3==0:
                n/=3
            elif n%3==1:
                n//=3
            else:
                return not flag
        return flag if n==0 else not flag


        