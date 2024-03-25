class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
    
        # Compute prefix sums
        prefix_sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sums[i][j] = mat[i - 1][j - 1] + prefix_sums[i - 1][j] + prefix_sums[i][j - 1] - prefix_sums[i - 1][j - 1]
        
        def get_sum(i, j):
            nonlocal prefix_sums, m, n, k
            x1, y1 = max(0, i - k), max(0, j - k)
            x2, y2 = min(m, i + k + 1), min(n, j + k + 1)
            return prefix_sums[x2][y2] - prefix_sums[x1][y2] - prefix_sums[x2][y1] + prefix_sums[x1][y1]
        
        # Compute the answer matrix
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get_sum(i, j)
        
        return ans