# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xl,yl = None, None
        queue = deque([(None, root)])
        level = 0

        while queue:
            for i in range(len(queue)):
                par, node = queue.popleft()

                if node.val == x:

                    xl = (level, par)

                if node.val == y:
                    yl = (level, par)

                if node.left:
                    queue.append((node.val, node.left))

                if node.right:
                    queue.append((node.val, node.right))
            level += 1
        
        return xl[0] == yl[0] and xl[1] != yl[1]