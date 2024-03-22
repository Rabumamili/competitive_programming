class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            idx = nums[i] -1
            if idx != i:
                if nums[idx] != nums[i]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                else:
                    i +=1
            else:
                i +=1
                    
        ans = []  
        for i in range(n):
            if nums[i] != i+1:
                ans.append(nums[i])
        return ans

