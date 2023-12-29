class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        maxim = float('-inf')

        for i in range(len(flips)):
            maxim= max(maxim, flips[i])
            if i + 1 == maxim:
                count += 1

        return count


        