class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1,1]
        for i in range(3, 38):
            nums.append((nums[i-1]+ nums[i-2]+nums[i-3]))
        return nums[n]