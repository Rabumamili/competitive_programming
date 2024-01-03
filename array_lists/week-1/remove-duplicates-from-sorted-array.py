class Solution:
    def removeDuplicates(self, nums ) :
        n=len(nums)
        if n == 0 or n == 1:
            return n
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
        
       