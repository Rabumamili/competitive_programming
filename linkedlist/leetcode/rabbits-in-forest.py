class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #  count the rabits who gave answer
        count = {}
        for ans in answers:
            count[ans] = count.get(ans, 0) + 1
        rabbits = 0
        for val in count:
            rabit = ceil(count[val]/(val+1))
            rabbits += (rabit*(val+1))
        return rabbits
        
        