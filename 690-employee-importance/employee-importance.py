"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if employees == []:
            return 0
        
        ans = 0
        hmap = {}
        for employee in employees:
            hmap[employee.id] = employee
        
        queue = deque()
        queue.append(id)
        while queue:
            employee = hmap[queue.popleft()]
            ans += employee.importance

            for subs in employee.subordinates:
                queue.append(subs)
        return ans