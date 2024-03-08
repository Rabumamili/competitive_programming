class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        maxim = max(counts.values())
        ans = 0
        for num in counts:
            if counts[num]==maxim:
                ans += maxim
        return ans
         
        return 1