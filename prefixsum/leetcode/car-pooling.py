class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_dist = max(max(trip[1], trip[2]) for trip in trips)

        locs = [0] * (max_dist + 1)

        for trip in trips:
            num_pass = trip[0]
            from_loc = trip[1]
            to_loc = trip[2]

            locs[from_loc] += num_pass
            locs[to_loc] -= num_pass
        # find the invalid
        passenger_count = 0
        for count in locs:
            passenger_count += count

            if passenger_count > capacity:
                return False

        return True
