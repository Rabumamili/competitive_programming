class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        array = set()
        for i in range(len(arr)):
            if (arr[i]/2) in array or arr[i]*2 in array:
                return True
            array.add(arr[i])
        return False