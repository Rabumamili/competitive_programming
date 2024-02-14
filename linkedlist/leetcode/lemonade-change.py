class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5:
            return False
        cash ={5:0, 10:0, 20:0}
        
        for i in range(len(bills)):
            if bills[i] == 5:
                cash[5] += 1
            elif bills[i] == 10:
                if cash[5]:   
                    cash[10] += 1
                    cash[5] -= 1
                else:
                    return False
            elif bills[i] == 20:
                if  cash[10] and cash[5]:
                    cash[10] -= 1
                    cash[5] -= 1
                    cash[20] += 1
                else:
                    if not cash[10] and cash[5] <3:
                        return False
                    elif not cash[10] and cash[5] >=3:
                        cash[5] -= 3
                        cash[20] += 1
                    elif cash[10] and not cash[5]:
                        return False
        return True

    