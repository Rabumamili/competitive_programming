class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)  # We only need to consider positive target values
        k = 0
        sum_k = 0
        
        while sum_k < target or (sum_k - target) % 2 != 0:
            k += 1
            sum_k += k
            
        return k