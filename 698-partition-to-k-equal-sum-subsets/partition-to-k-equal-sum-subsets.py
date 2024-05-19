class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        n = len(nums)
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False

        dp = [False] * (1 << n)
        dp[0] = True
        curr_sum = [0] * (1 << n)
        
        for mask in range(1 << n):
            if not dp[mask]:
                continue
            
            for i in range(n):
                if mask & (1 << i) == 0:
                    new_mask = mask | (1 << i)
                    if dp[new_mask]:
                        continue
                    
                    if curr_sum[mask] % target + nums[i] <= target:
                        dp[new_mask] = True
                        curr_sum[new_mask] = curr_sum[mask] + nums[i]
                        
                        if curr_sum[new_mask] % target == 0:
                            break
        
        return dp[(1 << n) - 1]