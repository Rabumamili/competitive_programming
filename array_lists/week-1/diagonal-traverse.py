 
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diag = defaultdict(list)

        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                diag[r + c].append(val)

        ans = []
        for k, values in diag.items():
            if k % 2:
                ans.extend(values)
            else:
                ans.extend(values[::-1])

        return ans