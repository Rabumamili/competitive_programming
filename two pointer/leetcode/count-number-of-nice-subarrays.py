class Solution(object):
    def numberOfSubarrays(self,nums, k):
        right = 0
        left = 0
        nice_subarrays = 0 
        odds = 0
        curr = 0
        for right in range(len(nums)):
            
            if nums[right]%2:
                odds += 1
                curr = 0
                
            while odds == k:
                if nums[left]%2 == 1:
                    odds -= 1
                curr += 1
                left += 1
                
            nice_subarrays += curr
            
        return nice_subarrays
     