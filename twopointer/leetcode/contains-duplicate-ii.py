class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}

        for i, num in enumerate(nums):
            if num in indexes and abs(i - indexes[num]) <= k:
                return True
            indexes[num] = i

        return False