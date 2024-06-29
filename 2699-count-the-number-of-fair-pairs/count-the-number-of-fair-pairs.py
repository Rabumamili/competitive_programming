class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  
        n = len(nums)
        count = 0
        
        for i in range(n - 1):
            low_bound = bisect_left(nums, lower - nums[i], i + 1)
            upper_bound = bisect_right(nums, upper - nums[i], i + 1) - 1
            
            if low_bound <= upper_bound:
                count += upper_bound - low_bound + 1
        
        return count
