class Solution:
     def findMaxAverage(self, nums , k ):
       
        sums = sum(nums[:k])                                  
        maxSums = sums
        for i in range(len(nums)-k):
            sums -= nums[i]
            sums += nums[i+k]
            maxSums = max(maxSums, sums)
        maxSums = float(maxSums)    
        return  maxSums/k