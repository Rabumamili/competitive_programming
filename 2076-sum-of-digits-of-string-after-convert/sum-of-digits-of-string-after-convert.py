class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''.join(str(ord(char) - ord('a') + 1) for char in s)
    
        for _ in range(k):
            num = str(sum(int(digit) for digit in num))
        
        return int(num)