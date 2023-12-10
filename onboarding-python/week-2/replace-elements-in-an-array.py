class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
    
        seen = {}
        n = len(nums)
        p = len(operations)
        
        for i in range(n):
            seen[nums[i]] = i
        
        for i in range(p):
            idx = seen.get(operations[i][0], None)
            
            if idx is not None:
                nums[idx] = operations[i][1]
                seen[operations[i][0]] = seen.pop(operations[i][0])
                seen[operations[i][1]] = idx
        
        return nums