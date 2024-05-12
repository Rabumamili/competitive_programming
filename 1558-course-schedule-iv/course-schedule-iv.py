class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])
        
        def bfs(course):
            visited = [False] * numCourses
            q = deque([course])
            
            while q:
                cur = q.popleft()
                visited[cur] = True
                for neigh in graph[cur]:
                    if not visited[neigh]:
                        q.append(neigh)
                        
            return visited
        
        isR = [[False] * numCourses for _ in range(numCourses)]
        for course in range(numCourses):
            isR[course] = bfs(course)
        
        answer = []
        for q in queries:
            u, v = q
            answer.append(isR[v][u])
        
        return answer