class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        newnums = sorted(set(nums))
        ans = 0
        for i, e in enumerate(newnums):
            ans += i * count[e]
        return ans