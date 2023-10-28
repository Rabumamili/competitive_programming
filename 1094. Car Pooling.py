class Solution(object):
    def carPooling(self, trips, capacity):
            
        max_distance = max(max(trip[1], trip[2]) for trip in trips)
    
        locations = [0] * (max_distance + 1)
    
        for trip in trips:
            num_passengers = trip[0]
            from_location = trip[1]
            to_location = trip[2]

            locations[from_location] += num_passengers
            locations[to_location] -= num_passengers
        passenger_count = 0
        for count in locations:
            passenger_count += count

            if passenger_count > capacity:
                return False
        return True

