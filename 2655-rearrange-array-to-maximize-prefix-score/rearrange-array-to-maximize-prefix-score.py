class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        prefixs =[nums[0]]
        for i in range(1,len(nums)):
            prefixs.append(prefixs[i-1]+nums[i])
        count = 0
        for j in range(len(prefixs)):
            if prefixs[j] > 0:
                count +=1
            else:
                break
        return count