class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        count = 0
        while i <=n:
            if n%i==0:
                count +=1
                if count==k:
                    return i
            i+=1
         
        return -1


 