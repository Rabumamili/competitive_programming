class Solution(object):
    
    def dividePlayers(self, skill ) :
        num_players = len(skill) 
        if num_players == 2:
            return skill[0] * skill[1]
        
        skill.sort()
        previous_sum = None
        result = 0
        
        for i in range(num_players // 2):
            j = num_players - i - 1
            
            if previous_sum is None:
                previous_sum = skill[i] + skill[j]
                result = skill[i] * skill[j]
            elif previous_sum == skill[i] + skill[j]:
                result += skill[i] * skill[j]
            else:
                return -1
        
        return result