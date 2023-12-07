class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
 
        n = len(nums)
        threshold = n // 3
        counter = Counter(nums)
        result = []

        for num, count in counter.items():
            if count > threshold:
                result.append(num)

        return result