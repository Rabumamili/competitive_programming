class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0]
        total = 1
        for start, end in points[1:]:
            if start > prev[1]:
                total +=1
                prev = [start, end]
            else:
                prev[1] = min(prev[1], end)
        return total

        