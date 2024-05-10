class Solution:
    def rob(self, nums: List[int]) -> int:
 
        if len(nums)==1:
            return nums[0]
         
        def dp(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return temp
        
        return max (dp(nums[1:]), dp(nums[:-1]))
        


        
            
         