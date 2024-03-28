class Solution:
    def brokenCalc(self, start: int, target: int) -> int: 
        if start >= target:
            return start - target
        count = 0
        while target > start:
            if target % 2:
                target += 1
                target //=2
                count += 2
            else:
                count += 1
                target //= 2
        if start > target:
            count += start - target
        return count
        