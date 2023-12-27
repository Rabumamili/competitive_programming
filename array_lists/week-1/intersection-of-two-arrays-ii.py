class Solution(object):
    def intersect(self, nums1, nums2):
    

    
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        intersection = []
        for num in counter1:
            if num in counter2:
                intersection.extend([num] * min(counter1[num], counter2[num]))
        
        return intersection
