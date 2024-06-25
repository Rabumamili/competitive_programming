class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(force):
            count = 1  
            end = position[0]
            
            for i in range(1, len(position)):
                if position[i] - end >= force:
                    count += 1
                    end = position[i]
                if count >= m:
                    return True
            return False
    
        position.sort()
        left, right = 1, position[-1] - position[0]
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans