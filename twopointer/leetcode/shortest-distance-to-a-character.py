class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer= [float('inf')] * n

        # Forward  
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], abs(i - prev))

        # Backward  
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], abs(i - prev))

        return answer