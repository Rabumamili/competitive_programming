class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
       
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        for row1 in range(rows):
            prefixSum = [0] * cols
            for row2 in range(row1, rows):
                for col in range(cols):
                    prefixSum[col] += matrix[row2][col]
                
                sumCount = {0: 1}
                currentSum = 0
                
                for col in range(cols):
                    currentSum += prefixSum[col]

                    if currentSum - target in sumCount:
                        count += sumCount[currentSum - target]

                    if currentSum in sumCount:
                        sumCount[currentSum] += 1
                        
                    else:
                        sumCount[currentSum] = 1

        return count