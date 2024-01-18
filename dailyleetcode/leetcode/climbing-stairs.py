class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

     
        first, second = 1, 1

        # Calculate ways to climb the staircase for each step
        for _ in range(2, n + 1):
            current = first + second
            first, second = second, current

        return second
