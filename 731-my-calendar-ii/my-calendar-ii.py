class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
         
        for o_start, o_end in self.overlaps:
            if max(start, o_start) < min(end, o_end):    
                return False
        for b_start, b_end in self.bookings:
            overlap_start = max(start, b_start)
            overlap_end = min(end, b_end)
            if overlap_start < overlap_end:   
                self.overlaps.append((overlap_start, overlap_end))   
        self.bookings.append((start, end))
        return True
