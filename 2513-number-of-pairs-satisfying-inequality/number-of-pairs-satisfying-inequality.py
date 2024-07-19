from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sorted_arr = SortedList()
        n = len(nums1)
        count = 0
        for i in range(n):
            greater = sorted_arr.bisect_right(nums1[i] - nums2[i]+ diff)
            count += greater
            sorted_arr.add(nums1[i]- nums2[i])
        return count