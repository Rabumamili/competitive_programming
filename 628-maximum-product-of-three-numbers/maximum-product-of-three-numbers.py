class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()

        maxi = max(nums[n - 3] * nums[n - 2] * nums[n - 1], nums[0] * nums[1] * nums[n - 1])

        return maxi 


            
            