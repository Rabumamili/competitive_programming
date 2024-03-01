class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums2[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
 
        while i < len(nums1):
            merged_array.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged_array.append(nums2[j])
            j += 1
        merged_array.sort()

        n = len(merged_array)
        if n ==1:
            return merged_array[0]/1
        if n%2:
            i = n//2
            return float(merged_array[i])
        else:
            i =n//2
            j = i-1
            return (merged_array[i] +merged_array[j])/2
 