class Solution(object):
    def checkSubarraySum(self, nums, k):
       prefix_sum=0
       seen={0:-1} #maps remainder and the end index of the prefix sum
        

       for i, n in enumerate(nums):
            prefix_sum += nums[i]
            remainder  = prefix_sum % k
            if remainder not in seen:
                seen[remainder] = i
                
            elif i - seen[remainder] > 1:
                return True
       return False