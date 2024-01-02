class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [a**2 + b**2 for a,b in points]
        sorted_distance= sorted(distance) 
        dlimit = sorted_distance[k-1]
        return [points[i] for i in range(len(points)) if distance[i]<= dlimit]