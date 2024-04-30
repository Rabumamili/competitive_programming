class Solution:
    def findComplement(self, num: int) -> int:
        binary = []
        while num >=1:
            if num%2:
                binary.append(0)
            else:
                binary.append(1)
            num = num//2
        num = 0
        for i in range(len(binary)-1, -1, -1):
            num += (binary[i]* 2**i)
        return num

        