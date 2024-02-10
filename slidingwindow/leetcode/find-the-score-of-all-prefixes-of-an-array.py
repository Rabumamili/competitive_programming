class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans =  [2*nums[0]]
        maxi = nums[0]
        
        for i in range (1, len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
            conver =  maxi + nums[i]
            prev = ans[i-1] 
            ans.append(prev + conver)
        return ans
