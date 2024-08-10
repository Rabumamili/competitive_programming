class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr.sort() 
        target.sort()
        if len(arr)!= len(target):
            return False
        for i in range(len(target)):
            if arr[i]!=target[i]:
                return False
        return True
