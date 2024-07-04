class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] != -1 and not dfs(leftChild[node]):
                return False
            if rightChild[node] != -1 and not dfs(rightChild[node]):
                return False
            return True
        
        visited = set()
        indegree = [0] * n
        
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
        
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False
        
        if root == -1:
            return False
        
        if not dfs(root):
            return False
        
        return len(visited) == n
