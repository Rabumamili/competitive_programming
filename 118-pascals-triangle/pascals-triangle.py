class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            
            row = [1]   
            if i > 0:
                for j in range(1, i):
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
                row.append(1)  
            triangle.append(row)
        
        return triangle