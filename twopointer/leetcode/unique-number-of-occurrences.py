class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mydict = {}
        for num in arr:
            if num in mydict:
                mydict[num] += 1
            else:
                mydict[num] = 1
        return len(mydict.values())==len(set(mydict.values()))