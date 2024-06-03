class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        nums.sort()
        res = set()
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  #skip duplicates
            seen = set()
            for j in range(i + 1, n):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.add((nums[i], nums[j], complement))
                seen.add(nums[j])
        
        return [list(triplet) for triplet in res]

    