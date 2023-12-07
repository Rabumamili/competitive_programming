class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        
        for j in range(len(positive)):
            nums[2*j] = positive[j]
            nums[2*j + 1] = negative[j]
            
        return nums
    
         
            