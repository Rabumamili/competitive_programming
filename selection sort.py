class Solution: 
    def select(self, nums, i):
        min_index = i
        n = len(nums)
        for j in range(i+1, n):
            if nums[j] < arr[min_index]:
                min_index = j
        return nums[min_index]
    
    def selectionSort(self, nums,n):
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i+1,len(nums)):
                if(nums[min_index] > nums[j]):
                    min_index = j
            nums[i],nums[min_index] = nums[min_index],nums[i]
