class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref_sum = [0]*(n+1)
        for st, end ,seat in bookings:
            pref_sum[st -1] += seat
            pref_sum[end] -= seat
        for i in range(1, n + 1):
            pref_sum[i] += pref_sum[i-1]
        return pref_sum[:-1]


