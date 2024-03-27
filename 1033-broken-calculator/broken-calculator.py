class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        def helper(startValue, target):
            if startValue >= target:
                return startValue - target

            if target %2 == 0:
                return 1 + helper(startValue, target/2)
            return 1 + helper(startValue, target+1)
        
        return int((helper(startValue, target)))
            