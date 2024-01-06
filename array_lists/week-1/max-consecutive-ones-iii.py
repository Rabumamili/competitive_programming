class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = 0
        best = 0

        for fast in range(len(nums)):

            while k<=0 and nums[fast] ==0:
                if nums[slow]==0:
                    k+=1
                slow +=1


            if nums[fast] ==0:
                k -=1
            best = max(best, (fast - slow)+ 1)
        return best 