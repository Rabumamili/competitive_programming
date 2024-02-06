class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * n
        
        for start, end in requests:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1

    
        for i in range(1, n):
            count[i] += count[i - 1]

        
        nums.sort(reverse=True)
        count.sort(reverse=True)

        # Calculate the maximum total sum modulo 10^9 + 7
        mod = 10**9 + 7
        total_sum = 0
        for i in range(n):
            total_sum = (total_sum + nums[i] * count[i]) % mod

        return total_sum