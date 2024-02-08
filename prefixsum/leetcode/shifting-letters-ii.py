class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
         
        accumulator = [0]*(len(s)+1)

        for start, end, direct in shifts: 
            if not direct: 
                accumulator[start] -= 1 
                accumulator[end+1] += 1    
            else: 
                accumulator[start] += 1 
                accumulator[end+1] -= 1


        prefix = 0
        ans = []

        for i, char  in enumerate(s): 
            prefix += accumulator[i]
            asci = (prefix + ord(char)-97)%26 + 97
            
            ans.append(chr(asci))

        return ''.join(ans)
        
       