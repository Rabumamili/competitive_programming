class Solution(object):
    def runningSum(self, nums):
        l=0
        r=0
        result=[]
        while l<len(nums):
            r+=nums[l]
            result.append(r)
            l+=1
            
        return result
