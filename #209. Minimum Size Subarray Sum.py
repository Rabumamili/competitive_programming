class Solution(object):
  def minSubArrayLen(self,target, nums):
    n = len(nums)
    min_length = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(n):
        window_sum += nums[right]
        
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    if min_length == float('inf'):
        return 0
    else:
        return min_length

 
