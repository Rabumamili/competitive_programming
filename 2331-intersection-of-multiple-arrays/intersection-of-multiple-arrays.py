class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict()
        n = len(nums)
        m = len(nums[0])
        for i in range(n):
            for j in range(len(nums[i])):
                if nums[i][j] in counts:
                    counts[nums[i][j]] += 1
                else:
                    counts[nums[i][j]] = 1


        ans = []
        for num in counts:
            if counts[num]==len(nums):
                ans.append(num)
        ans.sort()
        return ans
