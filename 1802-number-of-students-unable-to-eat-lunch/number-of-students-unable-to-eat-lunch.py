class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = [0, 0]  
        for x in students:
            c[x] += 1

        for y in sandwiches:
            if c[y] == 0:
                break   
            c[y] -= 1

        return sum(c)
