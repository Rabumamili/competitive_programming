class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
    
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        for i in range(n):
            if k > 0:
                for j in range(1, k + 1):
                  ans[i] += code[(i + j) % n]
            else:
                for j in range(1, abs(k) + 1):
                    ans[i] += code[(i - j) % n]

        return ans

        