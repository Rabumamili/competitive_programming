# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []

        while queue:
            n = len(queue)
            sums = 0
            for i in range(n):
                valu = queue.popleft()
                if valu:
                    sums += valu.val
                if valu and valu.left:
                    queue.append(valu.left)
                if valu and valu.right:
                    queue.append(valu.right)
        
            ans.append(sums/n)
        return ans