class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = Counter(arr)
        n = len(arr)/4
        for i in arr:
           if dic[i] > n:
               return i

