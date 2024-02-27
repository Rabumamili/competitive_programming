class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: 
            return [1]
        if rowIndex == 1: 
            return [1, 1]
        else:
            lis= self.getRow(rowIndex - 1)
            pascal = [1]
            for i in range(len(lis)-1):
                pascal.append(lis[i]+lis[i+1])
            pascal.append(1)
        return pascal