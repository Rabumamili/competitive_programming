class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 
        def backtrack(current, i):
            if i == len(nums):
                res.append(current[::])
                return 
            #  all subsets that include nums[i]
            current.append(nums[i])
            backtrack(current, i +1)
            current.pop()
            #  all subsets taht doesn't include nums[i]
            while i +1 < len(nums) and nums[i] ==nums[i+1]:
                i += 1
            backtrack(current,i+1)

        backtrack([], 0)

        return res