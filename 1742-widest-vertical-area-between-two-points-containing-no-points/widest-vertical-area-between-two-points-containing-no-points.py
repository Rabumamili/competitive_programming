class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    
        x = sorted(point[0] for point in points)
        max_width = max(x[i] - x[i-1] for i in range(1, len(x)))
        return  max_width 