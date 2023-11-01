class NumMatrix(object):

    def __init__(self, matrix):
         rows, cols = len(matrix), len(matrix[0])
         self.sumMat =[[0]*(cols +1) for c in range(rows +1)]
         for r in range (rows):
             prefix = 0
             for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]


                self.sumMat[r + 1][c +1] = prefix + above

    def sumRegion(self, r1, c1, r2, c2):
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1

        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2 ][c1 - 1]
        topLeft = self.sumMat[r1 -1][c1 - 1]

        return bottomRight - above - left + topLeft


         


 
