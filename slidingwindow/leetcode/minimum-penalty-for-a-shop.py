class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans= 0
        penality= 0
        
        for i in range(len(customers)):
            if customers[i] == 'Y':
                penality += 1

                if penality > 0:
                    ans = i + 1
                    penality = 0                
            else:
                penality -= 1
                    
        return ans
       