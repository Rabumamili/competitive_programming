class Solution:
    def isNumber(self, s: str) -> bool:
        state = [
            {},
            {'sign': 2, 'digit': 3, 'dot': 4},
            {'digit': 3, 'dot': 4},
            {'digit': 3, 'dot': 5, 'exp': 6},
            {'digit': 5},
            {'digit': 5, 'exp': 6},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8},
        ]
        
        currstate = 1
        for char in s:
            if '0' <= char <= '9':
                char_type = 'digit'
            elif char in '+-':
                char_type = 'sign'
            elif char in 'eE':
                char_type = 'exp'
            elif char == '.':
                char_type = 'dot'
            else:
                return False
            
            if char_type not in state[currstate]:
                return False
            
            currstate = state[currstate][char_type]

         
        return currstate in [3, 5, 8]