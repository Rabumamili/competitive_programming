class Solution:
    def dividePlayers(self, skill ) :
        num_players = len(skill) 
        if num_players == 2:
            return skill[0] * skill[1]
        
        skill.sort()
        left = 0
        right = num_players - 1
        result = 0
        
        while left < right:
            current_sum = skill[left] + skill[right]
            
            if left > 0 and current_sum != skill[left-1] + skill[right]:
                return -1
            
            result += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return result
