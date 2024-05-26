class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            boq = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        boq += 1
                        flowers = 0
                else:
                    flowers = 0
            
            return boq >= m
        
            if m * k > len(bloomDay):
                return -1
    
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if check(left) else -1