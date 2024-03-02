class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 1
        nums.sort()
        left = 0
        right = count = 1 
        while right < len(nums):
            if nums[right] - nums[left] > k:
                count +=1
                left = right
            right +=1
        return count

