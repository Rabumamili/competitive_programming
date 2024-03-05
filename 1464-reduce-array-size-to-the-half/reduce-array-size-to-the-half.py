class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) +1
        sortedval = sorted(counts.items(), key = lambda x:x[1], reverse = True)
        values = [value for _, value in sortedval]
        print(values)
        n = len(arr)
        i = 0
        sums = 0
        mid = n//2
        while n > mid and i < len(values):
            n = n-values[i]
             
            i +=1
        return i
        
            
        
             