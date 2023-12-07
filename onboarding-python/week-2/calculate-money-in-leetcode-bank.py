class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7  # Number of complete weeks
        remaining_days = n % 7  # Number of remaining days
        total = 0   
         
        for week in range(full_weeks):
            week_start = week + 1  
            week_end = week_start + 6  # Amount for the last day of the week
            week_total = (week_start + week_end) * 7 // 2  # Sum of arithmetic series
            total += week_total

        # Calculate the total amount for remaining days
        start_day = full_weeks + 1   
        
        for day in range(start_day, start_day + remaining_days):
            total += day

        return total