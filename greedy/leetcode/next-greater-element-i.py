class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxs = {}
        ans = [-1]*len(nums1)
        for i in range(len(nums2)):
            idxs[nums2[i]] = i
        for j in range(len(nums1)):
          
            for i in range(idxs[nums1[j]], len(nums2)):
                if nums2[i] > nums1[j]:
                    ans[j]= nums2[i]
                    break
        return ans
        
        