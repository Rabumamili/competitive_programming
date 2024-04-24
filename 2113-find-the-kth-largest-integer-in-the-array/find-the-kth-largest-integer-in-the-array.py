class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = [-(int(i)) for i in nums]
        heapify(num)
        while k > 1:
            heappop(num)
            k -= 1

        return str(-heappop(num))