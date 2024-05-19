class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        formatted = []
        res = [-1] * len(queries)
        for idx, query in enumerate(queries):
            a, b = query
            if a == b:
                res[idx] = a
            elif a < b and heights[a] < heights[b]:
                res[idx] = b
            elif b < a and heights[b] < heights[a]:
                res[idx] = a
            else:
                formatted.append((max(a, b), max(heights[a], heights[b]), idx))


        formatted.sort(reverse=True, key=lambda x: x[0])
        pt = len(heights) - 1
        stack = deque([])

        for rightmost, height, pos in formatted:
            for i in range(pt, rightmost, -1):
                while stack and heights[i] >= stack[0][0]:
                    stack.popleft()
                stack.appendleft((heights[i], i))
            pt = rightmost
            common = bisect_right(stack, height, key=lambda x: x[0])
            if common < len(stack):
                res[pos] = stack[common][1]
                
        return res

        