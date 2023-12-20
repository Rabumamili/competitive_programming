class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
     
        arr = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            row = []
            for j in range(m):
                row.append(matrix[j][i])
            arr.append(row)
        return arr
                