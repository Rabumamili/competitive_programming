class Solution:
    def climbStairs(self, n: int) -> int:
        end, prev = 1, 1
        for i in range(n-1):
            temp = end
            end = prev + end
            prev = temp
        return end
    
