class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
     
        result = []
        n = len(arr)
        for i in range(n - 1, 0, -1):
            max_index = arr.index(i + 1)
            if max_index != i:
                # Flip the subarray arr[0...max_index]
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
                result.append(max_index + 1)
                # Flip the entire unsorted part of the array arr[0...i]
                arr[:i + 1] = arr[:i + 1][::-1]
                result.append(i + 1)
        return result