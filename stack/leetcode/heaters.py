class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
    
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            
            if idx == 0:
                distance = abs(heaters[idx] - house)
            elif idx == len(heaters):
                distance = abs(heaters[idx - 1] - house)
            else:
                distance = min(abs(heaters[idx] - house), abs(heaters[idx - 1] - house))
            
            max_radius = max(max_radius, distance)
        
        return max_radius