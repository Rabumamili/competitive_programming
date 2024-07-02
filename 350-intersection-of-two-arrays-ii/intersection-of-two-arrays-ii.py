class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 =  Counter(nums2)
        ans = []
        for num in c2:
            if num in c1:
                ans.extend([num]*min (c1[num], c2[num]))
        return ans
        
