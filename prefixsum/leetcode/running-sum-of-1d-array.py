class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=0
        r=0
        result=[]
        while l<len(nums):
            r+=nums[l]
            result.append(r)
            l+=1
            
        return result