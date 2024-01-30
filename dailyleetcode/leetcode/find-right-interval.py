class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = [-1] * n

        ivls_idx = [(ivl, i) for i, ivl in enumerate(intervals)]
        ivls_idx.sort(key=lambda x: x[0][0])

        for i in range(n):
            target_end = intervals[i][1]
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2
                mid_start = ivls_idx[mid][0][0]

                if mid_start >= target_end:
                    res[i] = ivls_idx[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1

        return res
            