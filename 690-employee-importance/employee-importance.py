"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    res = 0
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hmap = collections.defaultdict(int)
        # create map if emp=> idx
        for i, emp in enumerate(employees):
            hmap[emp.id] = i

        self.dfs(employees, hmap[id], hmap)
        return self.res

    def dfs(self, employees, id, hmap):        
        self.res += employees[id].importance
        for sub_ord in employees[id].subordinates:
            self.dfs(employees,hmap[sub_ord], hmap)
        
        return self.res