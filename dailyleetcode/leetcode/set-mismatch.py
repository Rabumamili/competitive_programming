class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        dup = 0
        for num in nums:
            if num in seen:
                dup = num
                break
            seen.add(num)
        
         
        expected_sum = n * (n + 1) // 2
        actualsum = sum(nums)
        
        missing = expected_sum - actualsum + dup 
        
        return [dup , missing]
