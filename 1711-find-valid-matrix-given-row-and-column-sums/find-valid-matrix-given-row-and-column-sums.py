class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
  
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                # Determine the value to place in matrix[i][j]
                min_value = min(rowSum[i], colSum[j])
                matrix[i][j] = min_value
                
                # Update the row and column sums
                rowSum[i] -= min_value
                colSum[j] -= min_value
        
        return matrix
 