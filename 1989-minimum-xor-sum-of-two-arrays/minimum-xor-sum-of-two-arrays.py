class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [float('inf')] * (2**n)
        dp[0] = 0
        
        for mask in range(1 << n):
            x = bin(mask).count('1')
            for j in range(n):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + (nums1[x] ^ nums2[j]))
        
        return dp[(2**n) - 1]