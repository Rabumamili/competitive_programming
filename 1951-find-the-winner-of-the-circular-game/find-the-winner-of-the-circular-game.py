class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        mylist = [ i for i in range(1,n+1) ]
        j = 0
        while len(mylist) >1:
            # get the index to remove
            j = (j+ k-1) %len(mylist)
            mylist.pop(j)
        return mylist[0]



      