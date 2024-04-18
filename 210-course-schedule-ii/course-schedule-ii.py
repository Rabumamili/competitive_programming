class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incomings = [0 for _ in range(numCourses)]
        queue = deque()
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            incomings[course] +=1
        
        for i in range(len(incomings)):
            if incomings[i] ==0:
                queue.append(i)
                
                 
        while queue:
            course = queue.popleft()
            order.append(course)

            for pre in graph[course]:
                incomings[pre] -= 1
                if incomings[pre] == 0:
                    queue.append(pre)
                   
        if len(order) != numCourses:
            return []
        return order

            
        
       
        