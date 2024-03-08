class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
           
        # Binary search to find the insertion point of x in the array
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
       
        return arr[left:left+k]  