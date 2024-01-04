class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        ans = []
        count =0
       
        for i in range(0,len(tasks)-3,4):
            ans.append(processorTime[count]+tasks[i+3])
            
            count += 1

        return max(ans)
            