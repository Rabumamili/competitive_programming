class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = []
        flag = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i -j) >= indexDifference and abs(nums[j] - nums[i])>=valueDifference: 
                    return [i, j]
                     
        if len(ans)==0:
            return [-1, -1]
                    
                
        