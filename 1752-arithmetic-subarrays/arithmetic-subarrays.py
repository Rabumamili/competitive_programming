class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        
        for i in range(len(l)):
            subarray = sorted(nums[l[i]:r[i]+1])
            diff = subarray[1] - subarray[0]
            
            for j in range(1, len(subarray)):
                if subarray[j] - subarray[j-1] != diff:
                    result.append(False)
                    break
            else:
                result.append(True)
        
        if len(result) != len(l):
            result.append(False)
        
        return result
