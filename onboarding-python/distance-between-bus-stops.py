class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        cw_dist = 0
        ccw_dist = 0

        if destination > start:
            cw_dist = sum(distance[start:destination])
        else:
            cw_dist = sum(distance[start:]) + sum(distance[:destination])

        if destination < start:
            ccw_dist = sum(distance[destination:start])
        else:
            ccw_dist = sum(distance[destination:]) + sum(distance[:start])

        return min(cw_dist, ccw_dist)