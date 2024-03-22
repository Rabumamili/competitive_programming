class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        nums = [(n,i) for i,n in enumerate(nums)]
        res = [0]*len(nums)
        
        def mergesort(left,right):
            if left == right:
                return 
            mid = (left+right)//2
            mergesort(left,mid)
            mergesort(mid+1,right)
            
            i = left
            for j in range(mid+1,right+1):
                while i < mid+1 and nums[i][0] < nums[j][0]:
                    i += 1
                res[nums[j][1]] += i-left
       
            nums[left:right+1] = sorted(nums[left:right+1])
            
        mergesort(0,len(nums)-1) if nums else None
        return res[::-1]