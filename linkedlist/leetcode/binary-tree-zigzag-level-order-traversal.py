# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        if not root:
            return []

        result = []
        stack = [root]
        level = 0

        while stack:
            values = []
            next_level = []

            while stack:
                node = stack.pop()
                values.append(node.val)

                if level % 2 == 0:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            result.append(values)
            stack = next_level[:]
            level += 1

        return result