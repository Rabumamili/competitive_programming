class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zero = arr.count(0)
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:   
                if zero + i < len(arr):  
                    arr[zero + i] = 0
                if zero - 1 + i < len(arr):  # Shifted zero
                    arr[zero - 1 + i] = 0
                zero -= 1
            if i + zero < len(arr):   
                arr[zero + i] = arr[i]