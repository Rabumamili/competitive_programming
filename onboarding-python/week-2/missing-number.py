class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_number= max(nums)
        sum_nums= sum(nums)
        total= max_number*(max_number + 1)/2
        if total -sum_nums ==0:
            if 0 in nums:
                return int(max_number+1)
            if 0 not in nums:
                return 0
        else:
            return int(total-sum_nums)