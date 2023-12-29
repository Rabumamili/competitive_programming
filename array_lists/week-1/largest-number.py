 
class Solution:
     def largestNumber(self, nums: List[int]) -> str:
       
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for i in range(1 , len(nums)):
            newidx = i
            while (newidx > 0 and nums[newidx - 1] + nums[newidx] <= nums[newidx] + nums[newidx-1]):
                nums[newidx] , nums[newidx - 1] = nums[newidx - 1], nums[newidx]
                newidx -= 1
        
        result = "".join(nums)
        if (result in "0"*100):
            return "0"
        return result