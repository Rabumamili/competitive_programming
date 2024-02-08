class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixs =[0]*len(nums)
        sums = sum(nums)
        n = len(nums)
        cum_sum =0
        for i in range(n):
            if i == 0:
                prefixs[i] = 0
            else:
                cum_sum += nums[i-1]
                prefixs[i]= cum_sum
        suffix = 0
        for i in range(n):
            suffix = sums - prefixs[i] - nums[i]
            bef = nums[i]*i - prefixs[i]
            aft = suffix -(nums[i]*(n-i-1))
            prefixs[i] = bef + aft
        return prefixs





























        # suffix = 0
        # prefix = 0
        # for i in range(n):
        #     if i == 0:
        #         prefix = 0
        #         suffix = sum(nums) - nums[i]
                
        #     else:
        #         prefix+=nums[i-1]
        #         suffix = sum(nums) - prefix - nums[i]
        #     prev = (nums[i]*i) - prefix
        #     after = suffix - (nums[i]*(n-i-1))
        #     ans[i] = prev + after
        # return ans
