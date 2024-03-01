class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = 0
        ones = 0
        for char in s:
            if char == "1":
                ones += 1
            else:
                zeros += 1
        zeroPrefix = 0
        onePrefix = 0
        count = 0
        for char in s:
            if char == "0":
                count += onePrefix * (ones - onePrefix )
                zeroPrefix += 1
            else:
                count += zeroPrefix * (zeros - zeroPrefix)
                onePrefix += 1
        return count