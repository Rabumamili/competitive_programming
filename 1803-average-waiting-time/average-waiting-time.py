class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        available = 0
        total = 0
        for arrival, t in customers:
            available = max(available, arrival) + t
            total += available - arrival
        
        return total / len(customers)