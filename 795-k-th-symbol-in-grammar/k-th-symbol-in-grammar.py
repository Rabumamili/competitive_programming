class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        print(n ,k)
        if n==1:
            return 0
        leng = 2**(n-1)
        #  k is in the first half
        if k <=leng//2:
            return self.kthGrammar(n-1, k)
        else:
            newK = k- leng//2
            return 1-self.kthGrammar(n-1, newK)
        