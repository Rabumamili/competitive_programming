class Solution:
    def average(self, salary: List[int]) -> float:
        salary= sorted(salary)
        n= len(salary)
        total = sum(salary)
        total= total - (salary[0]+salary[n-1])
        return  (total/(n-2))
        
        