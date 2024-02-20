class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
 
        num_map = {}
        stack = [] #pair of val, index
        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            num_map[nums1[i]] = i

        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                res[num_map[val]] = nums2[i]
            if nums2[i] in num_map:
                stack.append(nums2[i])

        return res
        

            