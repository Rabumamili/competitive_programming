class Solution:
     def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False

        increasing = True

        for i in range(len(arr) - 1):
            if increasing:
                if arr[i] < arr[i+1]:
                    continue
                elif arr[i] == arr[i+1]:
                    return False
                else:
                    increasing = False
            else:
                if arr[i] <= arr[i+1]:
                    return False
        
        return not increasing