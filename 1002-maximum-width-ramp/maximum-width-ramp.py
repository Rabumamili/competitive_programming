class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        indices = sorted(range(len(nums)), key=lambda x: nums[x])
    
        max_width = 0
        min_index = float('inf')
        
        
        for index in indices:
           
            max_width = max(max_width, index - min_index)
            min_index = min(min_index, index)
            
        return max_width