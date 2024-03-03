class Solution:
 
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans=[]
        tracker1=set() # for column
        tracker2=set() # for positive diagonal 
        tracker3=set() # for negative diagonal 

        board=[["."]*n for i in range(n)]
        def helper(row):
            if row==n:
                currans=[]
                for roww in board:
                    rowAns="".join(roww)
                    currans.append(rowAns)
                ans.append(currans)
                return 
            for col in range(n):
                if col in tracker1 or col+row in tracker2 or row-col in tracker3:
                    continue
                board[row][col]="Q"
                tracker1.add(col)
                tracker2.add(col+row)
                tracker3.add(row-col)
                helper(row+1)
                tracker1.discard(col)
                tracker2.discard(col+row)
                tracker3.discard(row-col)
                board[row][col]="."
        helper(0)
        return ans 
        
            
            










        
        