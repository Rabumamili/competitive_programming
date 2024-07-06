class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = 1
        dirc = 1  
        for _ in range(time):
            pos += dirc
            if pos == n or pos == 1:
                dirc = -dirc

        return pos