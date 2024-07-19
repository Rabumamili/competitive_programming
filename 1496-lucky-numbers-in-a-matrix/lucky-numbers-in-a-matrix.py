class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_values = [min(row) for row in matrix]
        
        max_values = [max(col) for col in zip(*matrix)]
        
        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_values[i] and matrix[i][j] == max_values[j]:
                    lucky_numbers.append(matrix[i][j])
        
        return lucky_numbers