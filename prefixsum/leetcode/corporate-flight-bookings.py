class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixsum = [0]*(n+1)
        for st, end ,seat in bookings:
            prefixsum[st -1] += seat
            prefixsum[end] -= seat
        for i in range(1, n + 1):
            prefixsum[i] += prefixsum[i-1]
        return prefixsum[:-1]


