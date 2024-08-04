class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 1
        while n >=2:
            if n%2:
                count +=1
            n =n//2
        return count