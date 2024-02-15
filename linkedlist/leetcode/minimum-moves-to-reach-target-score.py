class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operations = 0
        while maxDoubles and target >= 1:
            if not target %2:
                maxDoubles -= 1
                target = target/2
                operations += 1
            else:
                target -= 1
                operations += 1
        operations += (target - 1)
        return int(operations)