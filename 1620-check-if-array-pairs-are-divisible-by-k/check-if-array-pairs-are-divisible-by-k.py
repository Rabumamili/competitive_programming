class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        freq , res = Counter(), 0
        
        for num in arr:
            if freq[-num%k]:
                res += 1
                freq[-num%k] -= 1
            else:
                freq[num%k] += 1
        return res ==n//2