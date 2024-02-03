class NumArray:

    
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1 )  # Initialize prefix sum array
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]
 
    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)