class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexMap = defaultdict(list)
        n = len(nums)
        res = [0] * n

        for i in range(n):
            indexMap[nums[i]].append(i)

        for vals in indexMap.values():
            if len(vals) > 1:
                m = len(vals)
                prefix = [0] * m
                suffix = [0] * m
                cur = 0

                for i in range(m):
                    cur += vals[i]
                    prefix[i] = cur

                cur = 0
                for i in range(m - 1, -1, -1):
                    cur += vals[i]
                    suffix[i] = cur

                for i in range(m):
                    res[vals[i]] = vals[i] * i - prefix[i] + suffix[i] - vals[i] * (m - 1 - i)

        return res