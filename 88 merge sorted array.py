class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = len(nums1)-1
        for i in range(len(nums2)-1, -1, -1):
            while m > 0 and nums2[i] < nums1[m-1]:
                nums1[total] = nums1[m-1]
                total -= 1
                m -= 1
            nums1[total] = nums2[i]
            total -= 1
