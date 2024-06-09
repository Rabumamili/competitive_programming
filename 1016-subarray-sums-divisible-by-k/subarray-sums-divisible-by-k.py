class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:
                mod += k
            if mod in prefix_sums:
                count += prefix_sums[mod]
            prefix_sums[mod] = prefix_sums.get(mod, 0) + 1

        return count
         
        