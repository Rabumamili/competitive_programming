class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        
        for i in range(n):
            count = 0
            
            for j in range(n):
                if boxes[j] == '1':
                    count += abs(j - i)
            
            ans[i] = count
        
        return ans