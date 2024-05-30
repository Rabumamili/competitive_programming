class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        n = len(arr)
        prefXOR = [0] * (n + 1)
        
        for i in range(n):
            prefXOR[i + 1] = prefXOR[i] ^ arr[i]
        
        count = 0
        
        for j in range(1, n):
            for i in range(j):
                if prefXOR[i] == prefXOR[j + 1]:
                    count += j - i
        
        return count

 