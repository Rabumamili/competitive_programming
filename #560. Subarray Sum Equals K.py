class Solution(object):
    def subarraySum(self,nums, k):
        count = 0
        cumulative_sum = 0
        sum_count = {0: 1}  
        for num in nums:
            cumulative_sum += num
            complement = cumulative_sum - k

            if complement in sum_count:
                count += sum_count[complement]

            if cumulative_sum in sum_count:
                sum_count[cumulative_sum] += 1
            else:
                sum_count[cumulative_sum] = 1

        return count
        
