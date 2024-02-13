class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            ans = []
            rows = len(matrix)
            cols = len(matrix[0])
            top, buttom, left,right = 0, rows-1, 0, cols-1
            while len(ans) < rows*cols:
                for i in range(left, right+1):
                    ans.append(matrix[top][i])
                top += 1
                for i in range(top, buttom+1):
                    ans.append(matrix[i][right])
                right -= 1
                if top <= buttom:
                    for i in range(right, left-1, -1):
                        ans.append(matrix[buttom][i])
                    buttom -= 1
                if left <= right:
                    for i in range(buttom, top-1,-1):
                        ans.append(matrix[i][left])
                    left += 1
            
            return ans