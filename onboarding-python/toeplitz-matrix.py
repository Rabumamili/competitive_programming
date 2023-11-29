class Solution(object):
    def isToeplitzMatrix(self, matrix):
   
        flag = False
        for row_idx, row in enumerate(matrix[:-1]):
            for col_idx, col in enumerate(row[:-1]):
                if col != matrix[row_idx + 1][col_idx + 1]:
                    flag = True
                    break
            if flag:
                break
        return not flag   
            