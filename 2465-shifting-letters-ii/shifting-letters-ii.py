class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        prefix = defaultdict(int)

        for i in shifts:
            prefix[i[0]]+=(2*i[2]-1)
            prefix[i[1]+1] -=(2*i[2]-1)
            
        prefix_sum = 0 
        for i in range(len(s)):
            prefix_sum+=prefix[i]
            s[i] = chr((((ord(s[i])+prefix_sum)-97)%26)+97)
        return "".join(s)
	