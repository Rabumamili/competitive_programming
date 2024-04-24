class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = [-i for i in nums]
        heapify(ans)
        while k > 1:
            heappop(ans)
            k -=1
        return -heappop(ans)