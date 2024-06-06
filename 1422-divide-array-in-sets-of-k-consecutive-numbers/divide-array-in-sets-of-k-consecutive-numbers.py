class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
    
        counts = Counter(nums)
        for num in sorted(counts):
            if counts[num] > 0:
                count = counts[num]
                for i in range(num, num + k):
                    if counts[i] < count:
                        return False
                    counts[i] -= count
        
        return True